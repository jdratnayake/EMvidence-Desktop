import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from application import Ui_MainWindow
import subprocess

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setGeometry(400,150,500,500)
        # self.setWindowTitle("EMvidence")
        # self.setWindowIcon(QIcon("logo.png"))
        # self.setToolTip("EMvidence")

        self.ui.button1.clicked.connect(self.collect_data)

    def collect_data(self):
        print("Button Clicked")
        samp_rate = self.ui.samp_rate.currentText()
        print(samp_rate)
        cent_freq_value = self.ui.cent_freq_value.toPlainText()
        # print(cent_freq_value)
        cent_freq_scale = self.ui.cent_freq_scale.currentText()
        print(cent_freq_value+cent_freq_scale)
        time = self.ui.time.toPlainText()
        print(time)

        
        args = ["python", "EM.py", "--samp_rate", samp_rate, "--cent_freq", cent_freq_value + cent_freq_scale, "--time", time]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            print("Subprocess output:")
            print(result.stdout)
            print("Data Collected! ")
        except subprocess.CalledProcessError as e:
            print(f"Subprocess failed with return code {e.returncode}")
            if e.returncode == 3221225477:
                print("Check if HackRF is connected")
            # print("Error output:")
            # print(e.stderr)   
    

def app():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

app()