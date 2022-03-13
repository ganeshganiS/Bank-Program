from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from ChatCentreUI import *
import sys


class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.bill)
        self.ui.pushButton_2.clicked.connect(self.reset)
        self.ui.pushButton_3.clicked.connect(self.exit)

        
    def bill(self):
        pp = int(self.ui.lineEdit.text())*20
        dh = int(self.ui.lineEdit_2.text())*30
        bp = int(self.ui.lineEdit_3.text())*30
        gm = int(self.ui.lineEdit_4.text())*70
        ct = int(self.ui.lineEdit_5.text())*30
        pb = int(self.ui.lineEdit_6.text())*50
        kch = int(self.ui.lineEdit_7.text())*45
        cd = int(self.ui.lineEdit_8.text())*22

        bill = pp+dh+bp+gm+ct+pb+kch+cd
        sgst = bill*0.09
        cgst = bill*0.09
        tot_bill = bill+sgst+cgst

        self.ui.label_11.setText("{:.2f}".format(bill))
        self.ui.label_12.setText("{:.2f}".format(sgst))
        self.ui.label_14.setText("{:.2f}".format(cgst))
        self.ui.label_16.setText("{:.2f}".format(tot_bill))
    def reset(self):
        self.ui.lineEdit.setText('0')
        self.ui.lineEdit_2.setText('0')
        self.ui.lineEdit_3.setText('0')
        self.ui.lineEdit_4.setText('0')
        self.ui.lineEdit_5.setText('0')
        self.ui.lineEdit_6.setText('0')
        self.ui.lineEdit_7.setText('0')
        self.ui.lineEdit_8.setText('0')

        self.ui.label_11.clear()
        self.ui.label_12.clear()
        self.ui.label_14.clear()
        self.ui.label_16.clear()
    def exit(self):
        sys.exit()
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = ChatApp()
    w.show()
    sys.exit(app.exec_())
