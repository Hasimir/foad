# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goad.ui'
#
# Created: Mon Oct 13 17:17:53 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_RunFOAD(object):
    def setupUi(self, RunFOAD):
        RunFOAD.setObjectName("RunFOAD")
        RunFOAD.resize(729, 894)
        self.verticalStackedWidget = QtGui.QStackedWidget(RunFOAD)
        self.verticalStackedWidget.setGeometry(QtCore.QRect(20, 70, 691, 301))
        self.verticalStackedWidget.setObjectName("verticalStackedWidget")
        self.verticalStackedWidgetPage1 = QtGui.QWidget()
        self.verticalStackedWidgetPage1.setObjectName("verticalStackedWidgetPage1")
        self.Fuck = QtGui.QLineEdit(self.verticalStackedWidgetPage1)
        self.Fuck.setGeometry(QtCore.QRect(0, 30, 691, 21))
        self.Fuck.setObjectName("Fuck")
        self.Extra = QtGui.QLineEdit(self.verticalStackedWidgetPage1)
        self.Extra.setGeometry(QtCore.QRect(0, 240, 691, 21))
        self.Extra.setObjectName("Extra")
        self.Target = QtGui.QLineEdit(self.verticalStackedWidgetPage1)
        self.Target.setGeometry(QtCore.QRect(0, 90, 691, 21))
        self.Target.setObjectName("Target")
        self.Sender = QtGui.QLineEdit(self.verticalStackedWidgetPage1)
        self.Sender.setGeometry(QtCore.QRect(0, 160, 691, 21))
        self.Sender.setObjectName("Sender")
        self.label = QtGui.QLabel(self.verticalStackedWidgetPage1)
        self.label.setGeometry(QtCore.QRect(1, 1, 321, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.verticalStackedWidgetPage1)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 241, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.verticalStackedWidgetPage1)
        self.label_3.setGeometry(QtCore.QRect(0, 130, 251, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.verticalStackedWidgetPage1)
        self.label_4.setGeometry(QtCore.QRect(0, 200, 241, 16))
        self.label_4.setObjectName("label_4")
        self.verticalStackedWidget.addWidget(self.verticalStackedWidgetPage1)
        self.dockWidget = QtGui.QDockWidget(RunFOAD)
        self.dockWidget.setGeometry(QtCore.QRect(-1, 0, 731, 80))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.toolBox = QtGui.QToolBox(self.dockWidgetContents)
        self.toolBox.setGeometry(QtCore.QRect(-1, 0, 731, 871))
        self.toolBox.setObjectName("toolBox")
        self.toolBoxPage1 = QtGui.QWidget()
        self.toolBoxPage1.setObjectName("toolBoxPage1")
        self.toolBox.addItem(self.toolBoxPage1, "")
        self.toolBoxPage2 = QtGui.QWidget()
        self.toolBoxPage2.setObjectName("toolBoxPage2")
        self.toolBox.addItem(self.toolBoxPage2, "")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.buttonBox = QtGui.QDialogButtonBox(RunFOAD)
        self.buttonBox.setGeometry(QtCore.QRect(530, 820, 181, 61))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtGui.QPushButton(RunFOAD)
        self.pushButton.setGeometry(QtCore.QRect(30, 830, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtGui.QTextBrowser(RunFOAD)
        self.textBrowser.setGeometry(QtCore.QRect(20, 370, 691, 441))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(RunFOAD)
        QtCore.QMetaObject.connectSlotsByName(RunFOAD)
        RunFOAD.setTabOrder(self.Fuck, self.Target)
        RunFOAD.setTabOrder(self.Target, self.Sender)
        RunFOAD.setTabOrder(self.Sender, self.Extra)
        RunFOAD.setTabOrder(self.Extra, self.textBrowser)

    def retranslateUi(self, RunFOAD):
        RunFOAD.setWindowTitle(QtGui.QApplication.translate("RunFOAD", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RunFOAD", "Type of fuck to give (required):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RunFOAD", "Name of target (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RunFOAD", "Name of sender (optional):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("RunFOAD", "Extra information (optional): ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("RunFOAD", "Clear Screen", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RunFOAD = QtGui.QWidget()
    ui = Ui_RunFOAD()
    ui.setupUi(RunFOAD)
    RunFOAD.show()
    sys.exit(app.exec_())

