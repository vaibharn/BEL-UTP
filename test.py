# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:24:35 2019

@author: Dell
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import pandas as pd
from threading import Thread
from queue import Queue 
import time

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800,800)
view = pg.GraphicsLayoutWidget()  
## GraphicsView with GraphicsLayout inserted by default
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
def update1():
    global data1, curve1, ptr1
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    #data1[-1] = np.random.normal()
    curve1.setData(data1)
    ptr1 += 1
    print(type(data1))
    
def update():
    update1()

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
def st():
    t1.start()
    t2.start() 

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()