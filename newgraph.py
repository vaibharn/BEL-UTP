# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:37:56 2019

@author: Dell
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QDesktopWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QComboBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas
import sys, psutil, time
from PyQt5.QtCore import pyqtSlot
from test import st


class Window(QDialog):
    
    
    

    def __init__(self):
        
        super().__init__()

        centerPoint = QDesktopWidget().availableGeometry().center()
        center_x = int(str(centerPoint)[-9:-6])
        center_y = int(str(centerPoint)[-4:-1])
        title = "Using Graphs inside GUI"
        left = center_x - 500
        top = center_y - 300
        width = 1000
        height = 600
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)
        self.UI()
        VBoxLayout = QVBoxLayout()
        VBoxLayout.addWidget(self.groupBox1)
        VBoxLayout.addWidget(self.groupBox2)
        self.setLayout(VBoxLayout)
        self.show()
    
    #for graph
    def UI(self):

        self.groupBox1 = QGroupBox()
        HBoxLayout1 = QHBoxLayout()
        pushButton = QPushButton("Generate Graph", self)
        #co =Canvas(self)
        pushButton.clicked.connect(on_click)        
        HBoxLayout1.addWidget(pushButton)
        self.groupBox1.setLayout(HBoxLayout1)
    #graph
        self.groupBox2 = QGroupBox()
        
        HBoxLayout2 = QHBoxLayout()
        self.groupBox2.setLayout(HBoxLayout2)
  
    #graph generation

class Canvas(FigureCanvasQTAgg):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        pass
    
    #@pyqtSlot()

def on_click():
    print("Called")
    st()
        
          
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())