# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:12:42 2019

@author: vaibh
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pandas as pd

win = pg.GraphicsWindow()
win.setWindowTitle('Scrolling Plots')
df=pd.read_csv('bitstampUSD_1-min_data_2012-01-01_to_2019-03-13.csv')
data1=df['Weighted_Price']

p2 = win.addPlot()
p2.setLabel('left', 'USD', '$')
p2.setLabel('bottom','Time','100000 mins')
curve1 = p2.plot(data1)

  
win.nextRow()
p4 = win.addPlot()
# Use automatic downsampling and clipping to reduce the drawing load
p4.setDownsampling(mode='peak')
p4.setClipToView(True)
curve2 = p4.plot()

data3=data1
ptr3 = 0

def update2():
    global data3, ptr3
    data3[ptr3] = np.random.normal()
    ptr3 += 100000
    if ptr3 >= data3.shape[0]:
        tmp = data3
        data3 = np.empty(data3.shape[0] * 2)
        data3[:tmp.shape[0]] = tmp
    curve2.setData(data3[:ptr3])

# update all plots
def update():
    if ptr3<3778817:
        update2()
    else:
        timer.stop()
timer = pg.QtCore.QTimer()
timer.start(1)
timer.timeout.connect(update)
    
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
