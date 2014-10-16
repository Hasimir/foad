#!/usr/bin/env python3

import sys
import subprocess
from PySide.QtCore import *
from PySide.QtGui import *

foad = "/usr/local/bin/foad.py"  # or code to find it

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.ed_1 = QLineEdit("WTF?")
        self.ed_2 = QLineEdit("Target")
        self.ed_3 = QLineEdit("Sender")
        self.ed_4 = QLineEdit("Extra")
        self.button = QPushButton("Run")
        layout = QVBoxLayout()
        layout.addWidget(self.ed_1)
        layout.addWidget(self.ed_2)
        layout.addWidget(self.ed_3)
        layout.addWidget(self.ed_4)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.sayFuck)

    def sayFuck(self):
        goad = []
        goad.append(foad)
        if len(self.ed_1.text()) > 0:
            gwtf = self.ed_1.text()
            goad.append("-f")
            goad.append(gwtf)
        else:
            goad.append("-h")
        if len(self.ed_2.text()) > 0:
            gtarget = self.ed_2.text()
            goad.append("-n")
            goad.append(gtarget)
        else:
            pass
        if len(self.ed_3.text()) > 0:
            gsender = self.ed_3.text()
            goad.append("-s")
            goad.append(gsender)
        else:
            pass
        if len(self.ed_4.text()) > 0:
            gextra = self.ed_4.text()
            goad.append("-e")
            goad.append(gextra)
        else:
            pass
        words = subprocess.Popen(goad, stdout=subprocess.PIPE).communicate()
        word = words[0]
        war = word.decode("utf-8").strip()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())

