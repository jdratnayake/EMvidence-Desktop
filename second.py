import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from application import Ui_MainWindow
import subprocess
import os
from PyQt5.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, args):
        super(WorkerThread, self).__init__()
        self.args = args

    def run(self):
        try:
            result = subprocess.run(self.args, capture_output=True, text=True, check=True)
            print("Subprocess output:")
            print(result.stdout)
            self.progress_updated.emit(100)  # Signal completion
        except subprocess.CalledProcessError as e:
            print(f"Subprocess failed with return code {e.returncode}")

            if e.returncode == 3221225477:
                # Handle hackrf error
                self.progress_updated.emit(-1)  # Signal hackrf error
            else:
                print("Error output:")
                print(e.stderr)
                self.progress_updated.emit(-2)  # Signal other error

class my_app(QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        project_location = os.path.dirname(os.path.abspath(__file__))
        self.project_location = project_location
        self.ui.path_text.setText(project_location)
        self.ui.progressBar.setVisible(False)
        self.ui.failed_group.setVisible(False)
        self.ui.successful_group.setVisible(False)
        self.ui.failed_group_hackrf.setVisible(False)
        self.ui.tick.setVisible(False)
        self.ui.cross_1.setVisible(False)
        self.ui.cross_2.setVisible(False)

        self.ui.button1.clicked.connect(self.collect_data)
        self.ui.path_button.clicked.connect(self.path_specify)

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
            return float(self.cent_freq_value)
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

        args = ["python", "EM.py", "--samp_rate", samp_rate, "--cent_freq", center_frequency, "--time", time_value, "--file", self.project_location]

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
    win = my_app()
    win.show()
    sys.exit(app.exec_())
