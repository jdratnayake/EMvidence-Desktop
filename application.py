# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 566)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(708, 566))
        MainWindow.setMaximumSize(QtCore.QSize(716, 566))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(55, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.samp_rate = QtWidgets.QComboBox(self.centralwidget)
        self.samp_rate.setEnabled(True)
        self.samp_rate.setGeometry(QtCore.QRect(231, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.samp_rate.setFont(font)
        self.samp_rate.setObjectName("samp_rate")
        self.samp_rate.addItem("")
        self.samp_rate.addItem("")
        self.samp_rate.addItem("")
        self.samp_rate.addItem("")
        self.samp_rate.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cent_freq_scale = QtWidgets.QComboBox(self.centralwidget)
        self.cent_freq_scale.setEnabled(True)
        self.cent_freq_scale.setGeometry(QtCore.QRect(410, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cent_freq_scale.setFont(font)
        self.cent_freq_scale.setObjectName("cent_freq_scale")
        self.cent_freq_scale.addItem("")
        self.cent_freq_scale.addItem("")
        self.cent_freq_scale.addItem("")
        self.cent_freq_scale.addItem("")
        self.cent_freq_value = QtWidgets.QTextEdit(self.centralwidget)
        self.cent_freq_value.setGeometry(QtCore.QRect(230, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cent_freq_value.setFont(font)
        self.cent_freq_value.setObjectName("cent_freq_value")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.time = QtWidgets.QTextEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(230, 170, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.time.setFont(font)
        self.time.setObjectName("time")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(230, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button1.setFont(font)
        self.button1.setDefault(False)
        self.button1.setObjectName("button1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_samp_rate = QtWidgets.QLabel(self.centralwidget)
        self.label_samp_rate.setGeometry(QtCore.QRect(70, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_samp_rate.setFont(font)
        self.label_samp_rate.setObjectName("label_samp_rate")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.path_text = QtWidgets.QLineEdit(self.centralwidget)
        self.path_text.setGeometry(QtCore.QRect(230, 300, 231, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.path_text.setFont(font)
        self.path_text.setText("")
        self.path_text.setObjectName("path_text")
        self.path_button = QtWidgets.QPushButton(self.centralwidget)
        self.path_button.setGeometry(QtCore.QRect(470, 300, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.path_button.setFont(font)
        self.path_button.setDefault(False)
        self.path_button.setObjectName("path_button")
        self.tick = QtWidgets.QLabel(self.centralwidget)
        self.tick.setGeometry(QtCore.QRect(151, 421, 25, 19))
        self.tick.setText("")
        self.tick.setPixmap(QtGui.QPixmap("resources/tick.png"))
        self.tick.setObjectName("tick")
        self.successful_group = QtWidgets.QLabel(self.centralwidget)
        self.successful_group.setGeometry(QtCore.QRect(182, 421, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.successful_group.setFont(font)
        self.successful_group.setObjectName("successful_group")
        self.cross_1 = QtWidgets.QLabel(self.centralwidget)
        self.cross_1.setGeometry(QtCore.QRect(151, 451, 22, 22))
        self.cross_1.setText("")
        self.cross_1.setPixmap(QtGui.QPixmap("resources/cross.png"))
        self.cross_1.setObjectName("cross_1")
        self.failed_group = QtWidgets.QLabel(self.centralwidget)
        self.failed_group.setGeometry(QtCore.QRect(180, 450, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.failed_group.setFont(font)
        self.failed_group.setObjectName("failed_group")
        self.cross_2 = QtWidgets.QLabel(self.centralwidget)
        self.cross_2.setGeometry(QtCore.QRect(321, 451, 22, 22))
        self.cross_2.setText("")
        self.cross_2.setPixmap(QtGui.QPixmap("resources/cross.png"))
        self.cross_2.setObjectName("cross_2")
        self.failed_group_hackrf = QtWidgets.QLabel(self.centralwidget)
        self.failed_group_hackrf.setGeometry(QtCore.QRect(349, 451, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.failed_group_hackrf.setFont(font)
        self.failed_group_hackrf.setObjectName("failed_group_hackrf")
        self.error_label_freq = QtWidgets.QLabel(self.centralwidget)
        self.error_label_freq.setGeometry(QtCore.QRect(230, 150, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.error_label_freq.setFont(font)
        self.error_label_freq.setObjectName("error_label_freq")
        self.error_label_time = QtWidgets.QLabel(self.centralwidget)
        self.error_label_time.setGeometry(QtCore.QRect(230, 210, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.error_label_time.setFont(font)
        self.error_label_time.setObjectName("error_label_time")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 240, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.file_name = QtWidgets.QTextEdit(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(230, 240, 161, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.file_name.setFont(font)
        self.file_name.setObjectName("file_name")
        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(260, 370, 91, 81))
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("resources/loading.gif"))
        self.loading.setObjectName("loading")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EMvidence"))
        self.samp_rate.setItemText(0, _translate("MainWindow", "20 MHz"))
        self.samp_rate.setItemText(1, _translate("MainWindow", "8 MHz"))
        self.samp_rate.setItemText(2, _translate("MainWindow", "10 MHz"))
        self.samp_rate.setItemText(3, _translate("MainWindow", "12.5 MHz"))
        self.samp_rate.setItemText(4, _translate("MainWindow", "16 MHz"))
        self.label.setText(_translate("MainWindow", "Center Frequency:"))
        self.cent_freq_scale.setItemText(0, _translate("MainWindow", "MHz"))
        self.cent_freq_scale.setItemText(1, _translate("MainWindow", "Hz"))
        self.cent_freq_scale.setItemText(2, _translate("MainWindow", "kHz"))
        self.cent_freq_scale.setItemText(3, _translate("MainWindow", "GHz"))
        self.label_2.setText(_translate("MainWindow", "Time duration: "))
        self.label_3.setText(_translate("MainWindow", "Seconds"))
        self.button1.setText(_translate("MainWindow", "Collect Data"))
        self.label_4.setText(_translate("MainWindow", "EMvidence Data Acquisition: "))
        self.label_samp_rate.setText(_translate("MainWindow", "Sampling Rate: "))
        self.label_5.setText(_translate("MainWindow", "Destination Folder:"))
        self.path_button.setText(_translate("MainWindow", "..."))
        self.successful_group.setText(_translate("MainWindow", "Data Collected Successfully!"))
        self.failed_group.setText(_translate("MainWindow", "Data Collection Failed!"))
        self.failed_group_hackrf.setText(_translate("MainWindow", "Hack RF connection Failed!"))
        self.error_label_freq.setText(_translate("MainWindow", "Invalid input type"))
        self.error_label_time.setText(_translate("MainWindow", "Invalid input type"))
        self.label_6.setText(_translate("MainWindow", "Filename:"))
