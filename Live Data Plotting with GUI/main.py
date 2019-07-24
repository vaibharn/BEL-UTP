# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:34:14 2019

@author: vaibh
"""

from PyQt5 import QtWidgets,QtCore
from PlotterMain import CustomWidget
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.widget = CustomWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 110, 800, 600))
        self.widget.setObjectName("widget")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.widget.lisfunc()
        self.ui.widget.tstart()
    
app = QtWidgets.QApplication([])
 
application = mywindow()
application.show()
sys.exit(app.exec())



