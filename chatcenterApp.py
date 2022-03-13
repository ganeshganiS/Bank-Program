from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from chatui import *
import sys

class chatcenter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BILL_1.clicked.connect(self.bill)
        self.ui.RESET_1.clicked.connect(self.reset)
        self.ui.EXIT_1.clicked.connect(self.exit)

    def bill(self):
        panipuri  =int(self.ui.paniPuri.text())*20
        Cutlet    =int(self.ui.CutLet.text())*30
        Pavbaji   =int(self.ui.PavBaji.text())*50
        Gobi_M    =int(self.ui.Gobi_Manchuria.text())*60
        BhelPuri  =int(self.ui.Bhel_Puri.text())*30
        cooldrinks=int(self.ui.Cool_Drinks.text())*25

        bill=panipuri+Cutlet+Pavbaji+Gobi_M+BhelPuri+cooldrinks
        SGST=bill*0.09
        CGST=bill*0.09
        Total_bill=bill+SGST+CGST

        self.ui.bill.setText("{:.2f}".format(bill))
        self.ui.sgst.setText("{:.2f}".format(SGST))
        self.ui.cgst.setText("{:.2f}".format(CGST))
        self.ui.total_bill.setText("{:.2f}".format(TOTAL_BILL))

    def reset(self):
        self.ui.paniPuri.setText("0")
        self.ui.CutLet.setText("0")
        self.ui.PavBaji.setText("0")
        self.ui.Gobi_Manchuria.setText("0")
        self.ui.Bhel_Puri.setText("0")
        self.ui.Cool_Drinks.setText("0")

        self.ui.bill.clear()
        self.ui.sgst.clear()
        self.ui.cgst.clear()
        self.ui.total_billbill.clear()

    def exit(self):
         sys.exit()        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = chatcenter()
    w.show()
    sys.exit(app.exec_())
