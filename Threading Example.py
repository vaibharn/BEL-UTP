# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:24:35 2019

@author: Dell
"""
from PyQt5 import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from threading import Thread
from queue import Queue 
import time

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800,800)
view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
mw.setCentralWidget(view)
mw.show()
mw.setWindowTitle('pyqtgraph example: ScatterPlot')
mw.show()
## create four areas to add plots

#w2 = view.addViewBox()
#w2.setAspectLocked(True)
#view.nextRow()
data1 = Queue(maxsize=100)
p1 = view.addPlot()
data1 = np.random.normal(size=100)
curve1 = p1.plot(data1)
ptr1 = 0
timer = pg.QtCore.QTimer()
def update():
    global data1, curve1, ptr1
    data1[:-1] = data1[1:]
    curve1.setData(data1)
    ptr1 += 1
    

#timer.timeout.connect(update)
#timer.start(500)  
 
def producer(out_q):
    while(True):
        print("producer")
        out_q[-1]=np.random.normal()
        time.sleep(0.5)

def consumer(in_q):    
    while(True):
        print("consumer")
        update()
        time.sleep(0.5)
    

t1 = Thread(target=consumer, args=(data1,)) 
t2 = Thread(target=producer, args=(data1,)) 
t1.start() 
t2.start()
 
import sys
sys.exit(app.exec())