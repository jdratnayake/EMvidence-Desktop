import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QColor, QMovie, QValidator, QRegExpValidator
from PyQt5.QtCore import QThread, pyqtSignal, QRegExp, QTimer
import subprocess
import osmosdr
from application import Ui_MainWindow
import time
import sys, os




class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, args):
        super().__init__()
        self.args = args

    def run(self):
        try:
            if not self.check_hackrf():
                raise ValueError("HackRF not found")
            result = subprocess.run(self.args, capture_output=True, text=True, check=True)
            print("Subprocess output:")
            print(result.stdout)
            self.progress_updated.emit(100)
        except ValueError as ve:
            self.progress_updated.emit(-1)
            print(f"Error: {ve}")
        except subprocess.CalledProcessError as e:
            print(f"Subprocess failed with return code {e.returncode}")
            if e.returncode == 3221225477:
                self.progress_updated.emit(-1)
                print(e.stderr)
            else:
                print("Error output:")
                print(e.stderr)
                self.progress_updated.emit(-2)

    def check_hackrf(self):
        try:
            available_devices = osmosdr.source().get_gain_names()
            if available_devices == None or 'RF' not in available_devices:
                return False
            return True
        except RuntimeError as e:
            print(e)
            return False

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # os.chdir(sys._MEIPASS)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.connect_signals()
        if sys.platform.startswith('linux'):
            if sys.version_info.major == 3:
                self.python_version = "python3"
            else:
                self.python_version = "python"    
        else:
            self.python_version = "python"

    def init_ui(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        project_location = application_path    
        # project_location = os.path.dirname(sys._MEIPASS)
        # project_location = os.path.dirname(os.path.abspath(__file__))
        self.ui.path_text.setText(project_location)
        self.ui.loading.setVisible(False)
        self.movie = QMovie('resources/loading.gif')
        self.movie.setSpeed(150)
        self.ui.loading.setMovie(self.movie)
        self.movie.start()
        self.ui.failed_group.setVisible(False)
        self.ui.successful_group.setVisible(False)
        self.ui.failed_group_hackrf.setVisible(False)
        self.ui.tick.setVisible(False)
        self.ui.cross_1.setVisible(False)
        self.ui.cross_2.setVisible(False)
        self.ui.file_name.setPlainText("signal.cfile")
        self.ui.error_label_freq.setStyleSheet("color: red;")
        self.ui.error_label_time.setStyleSheet("color: red;")
        self.ui.error_label_freq.setVisible(False)
        self.ui.error_label_time.setVisible(False)
        self.validation()
        self.ui.button1.setEnabled(False)
        self.freq_value_flag = False
        self.time_value_flag = False

    def connect_signals(self):
        self.ui.path_button.clicked.connect(self.path_specify)
        self.ui.button1.clicked.connect(self.handle_click)

    def handle_click(self):
        self.ui.loading.setVisible(True)
        QTimer.singleShot(1000, self.collect_data)


    def validation(self):
        validator_number = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.ui.cent_freq_value.textChanged.connect(lambda: self.validate_num(self.ui.cent_freq_value, validator_number, "freq_value_flag"))
        self.ui.time.textChanged.connect(lambda: self.validate_num(self.ui.time, validator_number, "time_value_flag"))

    def validate_num(self, text_edit, validator, flag_value):
        selected_text = text_edit.toPlainText()
        state = validator.validate(selected_text, 0)[0]

        if state == QValidator.Acceptable:
            self.check_enable_button(flag_value, text_edit)
        elif state == QValidator.Intermediate:
            self.ui.button1.setEnabled(False)
            self.error_input_validation(text_edit, flag_value, "empty")
        elif state == QValidator.Invalid:
            self.ui.button1.setEnabled(False)
            self.error_input_validation(text_edit, flag_value, "invalid")

    def error_input_validation(self, text_edit, flag_value, error_type):
        text_edit.setStyleSheet("QTextEdit{border: 1px solid red;}")
        if flag_value == "freq_value_flag":
            self.ui.error_label_freq.setVisible(True)
            self.ui.error_label_freq.setText("Please enter a value for Center Frequency" if error_type == "empty" else "")
        elif flag_value == "time_value_flag":
            self.ui.error_label_time.setVisible(True)
            self.ui.error_label_time.setText("Please enter a value for Time Duration" if error_type == "empty" else "")

    def check_enable_button(self, flag_value, text_edit):
        text_edit.setStyleSheet("QTextEdit{border: none;}")
        if flag_value == "freq_value_flag":
            self.freq_value_flag = True
            self.ui.error_label_freq.setVisible(False)
            if self.time_value_flag:
                self.ui.button1.setEnabled(True)
        elif flag_value == "time_value_flag":
            self.time_value_flag = True
            self.ui.error_label_time.setVisible(False)
            if self.freq_value_flag:
                self.ui.button1.setEnabled(True)

    def path_specify(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory:", self.ui.path_text.text())
        if folder_path:
            self.ui.path_text.setText(folder_path)

    def center_frequency_conversion(self, cent_freq_value, cent_freq_scale):
        conversions = {"Hz": 1, "kHz": 1e3, "MHz": 1e6, "GHz": 1e9}
        return float(cent_freq_value) * conversions.get(cent_freq_scale, 1)

    def handle_error_hackrf(self):
        self.ui.loading.setVisible(False)
        # self.movie.stop()
        self.show_message_box("HackRF Error", "Check if HackRF is connected")

    def handle_other_error(self):
        self.ui.loading.setVisible(False)
        # self.movie.stop()
        self.show_message_box("Other Error", "An error occurred during data collection")

    def handle_success(self):
        self.ui.loading.setVisible(False)
        # self.movie.stop()
        self.show_message_box("Data Collected", "Data collection successful")

    def show_message_box(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def get_sampling_rate(self,index):
        switch = {
            0: 20e6,
            1: 8e6,
            2: 10e6,
            3: 12.5e6,
            4: 16e6
        }
        return switch.get(index,None)


    def collect_data(self):
        samp_rate_index = self.ui.samp_rate.currentIndex()
        samp_rate = self.get_sampling_rate(samp_rate_index)
        print("Sampling rate: ")
        print(samp_rate)
        cent_freq_value = self.ui.cent_freq_value.toPlainText()
        cent_freq_scale = self.ui.cent_freq_scale.currentText()
        center_frequency = self.center_frequency_conversion(cent_freq_value, cent_freq_scale)
        time_value = self.ui.time.toPlainText()

        path = os.path.abspath(self.ui.path_text.text())
        file_name = self.ui.file_name.toPlainText()
        full_path = os.path.join(path, file_name)

        args = [self.python_version, "EM.py", "--samp_rate", str(samp_rate), "--cent_freq", str(center_frequency), "--time", str(time_value), "--file", str(full_path)]

        self.worker_thread = WorkerThread(args)
        self.worker_thread.progress_updated.connect(self.update_progress_bar)
        self.worker_thread.start()

    def update_progress_bar(self, value):
        if value == -1:
            self.handle_error_hackrf()
        elif value == -2:
            self.handle_other_error()
        else:
            self.handle_success()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
