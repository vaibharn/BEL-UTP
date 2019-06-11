# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:15:58 2019

@author: vaibh
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Bitcoin Historical Prices Scrolling Plot '
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Data taken from https://www.kaggle.com/mczielinski/bitcoin-historical-data')
        
        button=QPushButton("Generate Graph",self)
        button.setToolTip('Press the button to Generate a Scrolling Graph on the historical data on Bitcoin prices')
        button.move(300,240)
        button.clicked.connect(self.on_click)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        import BTCGraph
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())