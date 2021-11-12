#Clicking buttons -
# changes after press will be visible in terminal only

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("Clicked the Button !")

#function for a window
def window():
    #config setup for application - knows system configuration
    app = QApplication(sys.argv) 
    win = QMainWindow() #initialized a window
    #position of window on screen - (X,Y cordinates,dimensions x 2)
    win.setGeometry(200,200,600,500)
    win.setWindowTitle("Sample Project - This is Title") #window title

    #add text label - inside window
    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50,50) #position

    #buttons & clicks
    b1 = QtWidgets.QPushButton(win)
    b1.setText("CLICK ME")
    b1.clicked.connect(clicked) #after click effect


    #show and exit
    win.show()
    sys.exit(app.exec_())


#call fun
window()