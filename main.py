import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from application import Ui_MainWindow
import subprocess
import os
import time 
import threading

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
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
        # self.ui.button1.clicked.connect(lambda: self.ui.progressBar.setVisible(True))
        self.ui.path_button.clicked.connect(self.path_specify)

    def thread_function(self):
        print("Threading running")
        self.ui.progressBar.setVisible(True)


    def path_specify(self):
        folder_path = QFileDialog.getExistingDirectory(self,"Select Directory: ",self.ui.path_text.text())
        if folder_path:
            self.ui.path_text.setText(folder_path)
            self.project_location = folder_path
            print("Selected Path: "+folder_path)
        

    def center_frequency_conversion(self,cent_freq_value,cent_freq_scale):
        if cent_freq_scale == "Hz":
            return float(self.cent_freq_value)
        elif cent_freq_scale == "kHz":
            return float(cent_freq_value)*1e3
        elif cent_freq_scale == "MHz":
            return float(cent_freq_value)*1e6
        elif cent_freq_scale == "MHz":
            return float(cent_freq_value)*1e9 

    def handle_success(self):
        print("Data Collected! ")
        # self.ui.progressBar.setVisible(False)
        # self.ui.button1.setVisible(True)
        self.ui.successful_group.setGeometry(122, 411, 155, 19)
        self.ui.successful_group.setVisible(True)
        self.ui.tick.setGeometry(91, 411, 25, 19)
        self.ui.tick.setVisible(True)

    def handle_error_hackrf(self):
        print("Check if HackRF is connected")
        # self.ui.progressBar.setVisible(False)
        # self.ui.button1.setVisible(True)
        self.ui.failed_group_hackrf.setGeometry(120, 411, 149, 20)
        self.ui.failed_group_hackrf.setVisible(True)
        self.ui.cross_2.setGeometry(91, 411, 22, 22)
        self.ui.cross_2.setVisible(True)

    def handle_other_error(self):
        self.ui.failed_group.setGeometry(120, 411, 123, 20)
        self.ui.failed_group.setVisible(True)
        self.ui.cross_1.setGeometry(91, 411, 22, 22)
        self.ui.cross_1.setVisible(True)          



    def collect_data(self):
        print("Button Clicked")
        samp_rate = self.ui.samp_rate.currentText()
        print(samp_rate)
        cent_freq_value = self.ui.cent_freq_value.toPlainText()
        cent_freq_scale = self.ui.cent_freq_scale.currentText()
        print(cent_freq_value+cent_freq_scale)
        center_frequency = self.center_frequency_conversion(cent_freq_value,cent_freq_scale)
        center_frequency = str(center_frequency) 
        print("Center Frequency: "+center_frequency)       
        time = self.ui.time.toPlainText()
        print(time)


        
        args = ["python", "EM.py", "--samp_rate", samp_rate, "--cent_freq", center_frequency, "--time", time,"--file",self.project_location]
        print("Location: "+self.project_location)
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            print("Subprocess output:")
            print(result.stdout)
            self.handle_success()
            
        except subprocess.CalledProcessError as e:
            print(f"Subprocess failed with return code {e.returncode}")

            if e.returncode == 3221225477:
                self.handle_error_hackrf()
                
            else:
                print("Error output:")
                print(e.stderr)
                self.handle_other_error()
                
           
    

def app():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app()