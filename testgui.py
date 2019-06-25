# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:34:46 2019

@author: Dell
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Threaded Producer consumer based graph '
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('bel-upt')
        
        button=QPushButton("Generate Graph",self)
        button.setToolTip('Press the button to Generate a Scrolling graph')
        button.move(300,240)
        button.clicked.connect(self.on_click)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        from test import st
        st()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())