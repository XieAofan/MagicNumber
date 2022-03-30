import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import random
import time

import ui

class start():
    def __init__(self, ui):
        self.app = QApplication(sys.argv)
        self.ui = ui.Ui_mainWindow()
        self.start_n = 1
        self.end_n = 54
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.show)
        self.tn = 0
        self.pn = 0
        self.name = 'Name'

    def setup(self):
        MainWindow = QMainWindow()
        ui = self.ui
        ui.setupUi(MainWindow)
        MainWindow.show()
        ui.pushButton.clicked.connect(self.start_ramdom)
        sys.exit(self.app.exec_())

    def show(self):
        n = self.tn % self.end_n
        self.ui.lcdNumber.setProperty("intValue", n)
        if self.tn == self.pn:
            self.time.stop()
            _translate = QtCore.QCoreApplication.translate
            self.ui.label.setText(_translate("mainWindow", self.name))
            self.ui.pushButton.setEnabled(True)
        self.tn = self.tn + 1

    def start_ramdom(self):
        ui = self.ui
        tn = random.randint(self.start_n, self.end_n)
        self.tn = 0
        self.pn = tn+self.end_n*random.randint(1,2)
        '''
        while t < tn:
            #time.sleep(0.1)
            t = t + 1
            ui.lcdNumber.setProperty("intValue", t)
        '''
        self.ui.pushButton.setEnabled(False)
        self.time.start(20)


if __name__ == "__main__":
    n = start(ui)
    n.setup()


