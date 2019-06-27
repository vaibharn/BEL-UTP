from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QDesktopWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QRadioButton, QComboBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas
import numpy as np
import sys, psutil, time



class Window(QDialog):
    
    HBoxLayout1 = QHBoxLayout()
    HBoxLayout2 = QHBoxLayout()
    button_status = "Fixed Plot"
    stylelist = style.available
    tempa = np.zeros(1)

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
        label = QLabel("Select type of plot")
        VBoxLayout.addWidget(label)
        self.ComboBox = QComboBox()
        for item in self.stylelist:
            self.ComboBox.addItem(item)
        #self.ComboBox.currentTextChanged.connect(self.stylechange)
        VBoxLayout.addWidget(self.ComboBox)
        VBoxLayout.addWidget(self.groupBox3)
        self.setLayout(VBoxLayout)
        self.show()
        
    def return_pressed(self):
        l = self.textbox1.text()
        self.tempa[0]=l
        np.savetxt('file2.csv',self.tempa)
        
    def return_pressed2(self):
        l = self.textbox2.text()
        self.tempa[0]=l
        np.savetxt('file2.csv',self.tempa)
            #print(self.textbox1.text())

    def UI(self):

        self.groupBox1 = QGroupBox("Enter data")

        #radiobutton = QRadioButton("Fixed")
        #radiobutton.text = "Fixed Plot"
        
        #radiobutton.toggled.connect(self.buttonClick)
        #radiobutton = QRadioButton("Scrolling")
        #radiobutton.text = "Scrolling Plot"
        
        #radiobutton.toggled.connect(self.buttonClick)
        #self.groupBox1.setLayout(self.HBoxLayout1)
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20,20)
        self.textbox1.resize(280,20)
        self.HBoxLayout1.addWidget(self.textbox1)
        
        self.textbox2= QLineEdit(self)
        self.textbox2.move(320,20)
        self.textbox2.resize(280,20)
        self.HBoxLayout1.addWidget(self.textbox2)
        
        
         
        self.textbox1.returnPressed.connect(self.return_pressed) 
        self.textbox2.returnPressed.connect(self.return_pressed2) 
        
        

        

        self.groupBox3 = QGroupBox()

        self.groupBox3.setLayout(self.HBoxLayout2)

    
    """"def stylechange(self):
        stylename = self.ComboBox.currentText()
        print(f"Plot Style: {stylename}")
    
    
    def buttonClick(self):

        radio = self.sender()
        if radio.isChecked():
            print(f"Plot Type: {radio.text}")
            if radio.text == "Fixed Plot":
                self.button_status = "Fixed Plot"
            if radio.text == "Scrolling Plot":
                self.button_status = "Scrolling Plot"
                """
    
"""
    def fixed(self):

        canvas = Canvas(window, width = 8, height = 4)
        # canvas.move(0, 0)
        ani = animation.FuncAnimation(canvas.fig, canvas.fixedplot, interval = 1000)
        self.HBoxLayout2.addWidget(canvas)
    

    def scrolling(self):

        canvas = Canvas(window, width = 8, height = 4)
        # canvas.move(0, 0)
        ani = animation.FuncAnimation(canvas.fig, canvas.scrollingplot, interval = 1000)
        self.HBoxLayout2.addWidget(canvas) 
"""

class Canvas(FigureCanvasQTAgg):
    
    style.use("fivethirtyeight")
    fig = plt.figure()
        
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):

        # fig = Figure(figsize = (width, height), dpi = dpi)
        self.ax1 = self.fig.add_subplot(1, 1, 1)

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)
        
        
    

    def fixedplot(self, i):

        graph_data = pandas.read_csv("testdata1.csv")
        x_fixed = [x for x in graph_data["0"]]
        y_fixed = [y for y in graph_data["1"]]
        #updating csv
       
        
        self.ax1.clear()
        self.ax1.plot(x_fixed, y_fixed)
        
    

    def scrollingplot(self, i):
        k = 0
        x_scroll, y_scroll = [], []
        x_scrollupdate, y_scrollupdate = [], []
        x_scroll.append(k)
        y_scroll.append(psutil.cpu_percent())
        if len(x_scroll) < 15:
            # self.ax1.clear()            
            self.ax1.plot(x_scroll, y_scroll)
            k += 1
        else:
            x_scrollupdate.append(x_scroll[-10::])
            y_scrollupdate.append(y_scroll[-10::])
            self.ax1.plot(x_scrollupdate, y_scrollupdate)
            k += 1



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    canvas = Canvas(window, width = 8, height = 4, dpi = 100)
    while True:
        if window.button_status == "Fixed Plot":
            ani = animation.FuncAnimation(canvas.fig, canvas.fixedplot, interval = 1000)
            window.HBoxLayout2.addWidget(canvas)
        if window.button_status == "Scrolling Plot":
            ani = animation.FuncAnimation(canvas.fig, canvas.scrollingplot, interval = 1000)
            window.HBoxLayout2.addWidget(canvas)
        sys.exit(App.exec())
        plt.show()