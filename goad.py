#!/usr/bin/env python3

# This is a GUI wrapper for foad.py which calls that script as an
# ordinary script instead of trying to import it.
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

        fuck = QLabel(self.tr("Enter type of fuck to give (required, one word)"))
        self.fle = QLineEdit()
        self.fte = QTextEdit()

        target = QLabel(self.tr("Enter the name of the person or entity directed at (if any)"))
        self.tle = QLineEdit()
        self.tte = QTextEdit()

        sender = QLabel(self.tr("Enter the name of the sender (optional)"))
        self.sle = QLineEdit()
        self.ste = QTextEdit()

        extra = QLabel(self.tr("Enter extra data to augment fuck type or append to message (optional)"))
        self.ele = QLineEdit()
        self.ete = QTextEdit()

        layout = QVBoxLayout(self)
        layout.addWidget(fuck)
        layout.addWidget(self.fle)
        layout.addWidget(self.fte)
        layout.addWidget(target)
        layout.addWidget(self.tle)
        layout.addWidget(self.tte)
        layout.addWidget(sender)
        layout.addWidget(self.sle)
        layout.addWidget(self.ste)
        layout.addWidget(extra)
        layout.addWidget(self.ele)
        layout.addWidget(self.ete)
        self.setLayout(layout)

        self.fullcmd = "foad.py -f {0} -n {1} -s {2} -e {3}".format(self.fle, self.tle, self.sle, self.ele)

        self.connect(self.fullcmd, SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        cmd = str(self.fullcmd.text())
        stdouterr = subprocess.Popen(["foad.py", "-f", self.fle, "-n",
                                      self.tle, "-s", self.sle, "-e",
                                      self.ele], stdout=subprocess.PIPE)
        self.te.setText(stdouterr.stdout.read().decode("UTF-8"))

if __name__ == "__main__":
    main()

# clearly not working yet, but the aim is to have seperate text boxes
# for each argparse flag.
