from PyQt5 import QtGui
import pyqtgraph as pg
import numpy as np 
from threading import Thread
from queue import Queue 
import time

class  CustomWidget(pg.GraphicsWindow):
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    data1 = Queue(maxsize=100)
    ptr1 = 0
    stop_t = False 
    def __init__(self, parent=None, **kargs):
        pg.GraphicsWindow.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle('pyqtgraph randomly generated data')
        p1 = self.addPlot(labels =  {'left':'y-axis', 'bottom':'x-axis'})
        self.data1 = np.random.normal(size=100)
        self.curve1 = p1.plot(self.data1,pen='g')
        self.t1 = Thread(target=self.consumer, args=(self.data1,)) 
        self.t2 = Thread(target=self.producer, args=(self.data1,))
        
    def update(self):
        self.data1[:-1] = self.data1[1:]
        self.curve1.setData(self.data1)
        self.ptr1 += 1
    
    def producer(self,out_q):
        while(True):
            print("producer")
            out_q[-1]=np.random.normal()
            time.sleep(0.5)

    def consumer(self,in_q):    
        while(True):
            print("consumer")
            self.update()
            time.sleep(0.5)
            
    def tstart(self):
        self.t1.start() 
        self.t2.start()
    
    
    def closeEvent(self, event):
        self.t2._stop()
        self.t1._stop()
        self.deleteLater()

if __name__ == '__main__':
    w = CustomWidget()
    w.show()
    w.tstart()
    QtGui.QApplication.instance().exec_()