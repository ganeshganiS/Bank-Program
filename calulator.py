from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from calcui import *
import sys
from math import *

class calucator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_11.clicked.connect(self.submit)
        self.ui.pushButton_12.clicked.connect(self.reset)
        self.ui.pushButton_13.clicked.connect(self.exit)

    def submit(self):
        s=self.ui.lineEdit.text()
        self.ui.label_5.setText(str(eval(s)))
        
    def reset(self):
        self.ui.lineEdit.clear()
        self.ui.label_5.clear()
        
    def exit(self):
        sys.exit()



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = calucator()
    w.show()
    sys.exit(app.exec_())
