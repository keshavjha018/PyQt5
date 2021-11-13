from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#to show changes on window (after pressing button),
# we need to define tasks inside class 

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setGeometry(200,200,600,500)
        self.setWindowTitle("Sample Project - This is Title")
        self.initUI()

    def initUI(self):
        #all stuff we want to put inside window
        
        self.label = QtWidgets.QLabel(self) #bcz obj is actual window
        self.label.setText("My first label")
        self.label.move(50,50) #position

        #buttons & clicks
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("CLICK ME")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('You pressed the button')
        self.update()

    #automatically adjust size of label
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv) 
    win = mywindow()
    
    #show and exit
    win.show()
    sys.exit(app.exec_())


window()

"""
to show changes on label after pressing button
we need to change the contents of label
to do that we created a class
"""