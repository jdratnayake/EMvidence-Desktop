import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon, QRegExpValidator,QValidator, QPalette, QColor, QTextCursor

from application import Ui_MainWindow
import subprocess
import os
from PyQt5.QtCore import QThread, pyqtSignal, QRegExp,Qt
import osmosdr



class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, args):
        super(WorkerThread, self).__init__()
        self.args = args

    def run(self):
        try:
            if not self.check_hackrf():
                raise ValueError("HackRF not found")
            result = subprocess.run(self.args, capture_output=True, text=True, check=True)
            print("Subprocess output:")
            print(result.stdout)
            self.progress_updated.emit(100)
              # Signal completion
        except ValueError as ve:
            self.progress_updated.emit(-1)
            print(f"Error: {ve}")   
        except subprocess.CalledProcessError as e:
            print(f"Subprocess failed with return code {e.returncode}")

            if e.returncode == 3221225477:
                # Handle hackrf error
                self.progress_updated.emit(-1)
                print(e.stderr)  # Signal hackrf error
            else:
                print("Error output:")
                print(e.stderr)
                self.progress_updated.emit(-2)  # Signal other error


    def check_hackrf(self):
        
        try:
            print("Ckecking if Hack RF is connected")
            available_devices = osmosdr.source().get_gain_names()
            if 'RF' in available_devices:
                return True
            else:
                return False
            # print(available_devices)
        except RuntimeError as e:
            print("No Supported device found")
            return False                 

class my_app(QMainWindow):
    def __init__(self):    
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        project_location = os.path.dirname(sys.executable)
        self.project_location = project_location
        self.ui.path_text.setText(project_location)
        self.ui.progressBar.setVisible(False)
        self.ui.failed_group.setVisible(False)
        self.ui.successful_group.setVisible(False)
        self.ui.failed_group_hackrf.setVisible(False)
        self.ui.tick.setVisible(False)
        self.ui.cross_1.setVisible(False)
        self.ui.cross_2.setVisible(False)
        self.ui.file_name.setPlainText("signal.cfile")
        
        self.ui.error_label_freq.setStyleSheet("color: red;")
        self.ui.error_label_freq.setVisible(False)
        self.ui.error_label_time.setStyleSheet("color: red;")
        self.ui.error_label_time.setVisible(False)
        self.validation()
        self.ui.button1.setEnabled(False)
        self.freq_value_flag = False
        self.time_value_flag = False

        self.ui.button1.clicked.connect(self.collect_data)
        self.ui.path_button.clicked.connect(self.path_specify)

    def validation(self):
        validator_number = QRegExpValidator(QRegExp(r'[0-9]+'))
        self.ui.cent_freq_value.textChanged.connect(lambda: self.validate_num(self.ui.cent_freq_value,validator_number,"freq_value_flag"))
        self.ui.time.textChanged.connect(lambda: self.validate_num(self.ui.time,validator_number,"time_value_flag"))

    def validate_num(self, text_edit, validator,flag_value):
        print(flag_value)
        cursor = text_edit.textCursor()
        cursor.movePosition(cursor.StartOfBlock,cursor.KeepAnchor)
        selected_text = text_edit.toPlainText()

        pos = 0
        state = validator.validate(selected_text,pos)[0]

        if state == QValidator.Acceptable:
            print("Input is valid.")
            self.check_enable_button(flag_value,text_edit)
            # self.check_enable_button()
        elif state == QValidator.Intermediate:
            print("Input is empty.")
            self.ui.button1.setEnabled(False)
            self.error_input_validation(text_edit,flag_value,"empty")

        elif state == QValidator.Invalid:
            print("Input is invalid.")
            self.ui.button1.setEnabled(False)
            self.error_input_validation(text_edit,flag_value,"invalid")

    def error_input_validation(self,text_edit,flag_value,error_type):
        # Set the border color to red
        border_color = QColor(255, 0, 0)
        style_sheet = f"QTextEdit{{border: 1px solid {border_color.name()};}}"
        text_edit.setStyleSheet(style_sheet)
        if flag_value == "freq_value_flag":
            if error_type == "invalid":
                self.ui.error_label_freq.setVisible(True)
            elif error_type == "empty":
                self.ui.error_label_freq.setText("Please enter a value for Center Frequency")
                self.ui.error_label_freq.setVisible(True)    
        elif flag_value == "time_value_flag":
            if error_type == "invalid":
                self.ui.error_label_time.setVisible(True)
            elif error_type == "empty":
                self.ui.error_label_time.setText("Please enter a value for Time Duration")
                self.ui.error_label_time.setVisible(True)

    
    def check_enable_button(self,flag_value,text_edit):
        # Things needed to be validated
        # self.ui.cent_freq_value
        # self.ui.time
        style_sheet_none = "QTextEdit{border: none;}"
        text_edit.setStyleSheet(style_sheet_none)
        if flag_value == "freq_value_flag": 
            self.freq_value_flag = True
            self.ui.error_label_freq.setVisible(False)
            if self.time_value_flag == True:
               self.ui.button1.setEnabled(True)
               
        elif flag_value == "time_value_flag":
            self.time_value_flag = True
            self.ui.error_label_time.setVisible(False)
            if self.freq_value_flag == True:
                self.ui.button1.setEnabled(True)       

    def thread_function(self):
        print("Threading running")
        self.ui.progressBar.setVisible(True)

    def path_specify(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory: ", self.ui.path_text.text())
        if folder_path:
            self.ui.path_text.setText(folder_path)
            self.project_location = folder_path
            print("Selected Path: " + folder_path)

    def center_frequency_conversion(self, cent_freq_value, cent_freq_scale):
        if cent_freq_scale == "Hz":
            return float(cent_freq_value)
        elif cent_freq_scale == "kHz":
            return float(cent_freq_value) * 1e3
        elif cent_freq_scale == "MHz":
            return float(cent_freq_value) * 1e6
        elif cent_freq_scale == "GHz":
            return float(cent_freq_value) * 1e9

    def handle_success(self):
        print("Data Collected! ")
        self.ui.successful_group.setGeometry(122, 411, 155, 19)
        self.ui.successful_group.setVisible(True)
        self.ui.tick.setGeometry(91, 411, 25, 19)
        self.ui.tick.setVisible(True)
        self.ui.progressBar.setVisible(False)

    def handle_error_hackrf(self):
        print("Check if HackRF is connected")
        self.ui.failed_group_hackrf.setGeometry(120, 411, 149, 20)
        self.ui.failed_group_hackrf.setVisible(True)
        self.ui.cross_2.setGeometry(91, 411, 22, 22)
        self.ui.cross_2.setVisible(True)
        self.ui.progressBar.setVisible(False)

    def handle_other_error(self):
        self.ui.failed_group.setGeometry(120, 411, 123, 20)
        self.ui.failed_group.setVisible(True)
        self.ui.cross_1.setGeometry(91, 411, 22, 22)
        self.ui.cross_1.setVisible(True)
        self.ui.progressBar.setVisible(False)

    def collect_data(self):
        self.ui.progressBar.setValue(0)  # Reset progress bar
        self.ui.progressBar.setVisible(True)

        samp_rate = self.ui.samp_rate.currentText()
        cent_freq_value = self.ui.cent_freq_value.toPlainText()
        cent_freq_scale = self.ui.cent_freq_scale.currentText()
        center_frequency = self.center_frequency_conversion(cent_freq_value, cent_freq_scale)
        center_frequency = str(center_frequency)
        time_value = self.ui.time.toPlainText()

        path = self.ui.path_text.text()
        path = os.path.abspath(path)
        file_name = self.ui.file_name.toPlainText()
        full_path = os.path.join(path, file_name)
        print("File path: "+full_path)
        if sys.version_info.major == 2:
            pythonVar = "python3"
        elif sys.version_info.major == 3:
            pythonVar = "python"

        args = [pythonVar, "EM.py", "--samp_rate", samp_rate, "--cent_freq", center_frequency, "--time", time_value, "--file", full_path]

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
    os.chdir(sys._MEIPASS)
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())
