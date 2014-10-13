#!/usr/bin/env python3

import subprocess
import sys
from PySide.QtCore import *
from PySide.QtGui import *

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        label = QLabel(self.tr("Enter command and press Return"))
        self.le = QLineEdit()
        self.te = QTextEdit()

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout)

        self.connect(self.le, SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        cmd = str(self.le.text())
        stdouterr = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        self.te.setText(stdouterr.stdout.read().decode("UTF-8"))

if __name__ == "__main__":
    main()

