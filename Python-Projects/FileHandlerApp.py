from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from FileHandlerUI import *

class File(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.save)
        self.ui.pushButton_2.clicked.connect(self.exit)
    def save(self):
        f = open("FileLog.txt","a")
        t = self.ui.lineEdit.text()
        f.write(t+"\n")
        self.reset()
    def exit(self):
        f.close()
        sys.exit()
    def reset(self):
        self.ui.lineEdit.clear()
  

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = File()
    f = open("FileLog.txt","a")
    w.show()
    sys.exit(app.exec_())

