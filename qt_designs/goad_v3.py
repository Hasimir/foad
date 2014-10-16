#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goad_draft_03.ui'
#
# Created: Fri Oct 17 07:40:44 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import subprocess
import sys
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 30, 501, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 211, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 70, 501, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 201, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 110, 501, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 211, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 150, 501, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 101, 16))
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 340, 741, 192))
        self.textBrowser.setObjectName("textBrowser")

        def callFoad():
            if self.lineEdit.text() is not None:
                gwtf = self.label.setText(self.lineEdit.text())
            else:
                gwtf = "random"
            if self.lineEdit_2.text() is not None:
                gtarget = self.label_2.setText(self.lineEdit_2.text())
            else:
                gtarget = ""
            if self.lineEdit_3.text() is not None:
                gsender = self.label_3.setText(self.lineEdit_3.text())
            else:
                gsender = ""
            if self.lineEdit_4.text() is not None:
                gextra = self.label_4.setText(self.lineEdit_4.text())
            else:
                gextra = ""
            with subprocess.Popen(["foad.py", "-f", gwtf, "-n", gtarget,
                                   "-s", gsender, "-e", gextra],
                                  stdout=subprocess.PIPE) as gfoad:
                gfuck = gfoad.decode("utf-8").strip()
            self.textBrowser.setText(gfuck)
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 190, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(callFoad())
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 190, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(sys.exit())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Type of fuck to give (required):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Name of target (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Name of sender (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Extra data (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Output:", None, QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
