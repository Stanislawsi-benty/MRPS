import pathlib
from Air_db.savedb import *
from pathlib import Path
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from Interfaces.mainWindowcashier import Ui_MainWindow
from Interfaces.Revenue import Ui_CashRevenue
from Interfaces.buy_tic import Ui_buy_tic
from Interfaces.vozv_tic import Ui_vozv_tic
import sys


# ___________Основное окно пользователя___________#


class UserMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_buy_tic.clicked.connect(self.activatebuy)
        self.ui.btn_vozv_tic.clicked.connect(self.returnticket)
        self.ui.btn_revenue.clicked.connect(self.revenue)

    def activatebuy(self):
        userwindow.close()
        buywindow.show()

    def returnticket(self):
        userwindow.close()
        returnticket.show()

    def revenue(self):
        userwindow.close()
        revenuewin.show()


        #____________окно подсчета выручки_________#


class Revenue(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CashRevenue()
        self.ui.setupUi(self)

        self.ui.back_button.clicked.connect(self.backmenu)

    def backmenu(self):
        revenuewin.close()
        userwindow.show()

        # ___________Окно покупки билета___________#


class BuyTicket(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_buy_tic()
        self.ui.setupUi(self)

        self.ui.lineEdit
        self.ui.lineEdit_2
        self.ui.lineEdit_3
        self.ui.lineEdit_4
        self.ui.lineEdit_5
        self.ui.lineEdit_6
        self.ui.box_gender

        self.savedatadb = Save()

        self.ui.but_buy.clicked.connect(self.buyticket)
        self.ui.but_buy_2.clicked.connect(self.backmenu)

    def buyticket(self):
        surname = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        familia = self.ui.lineEdit_3.text()
        grajdanstwo = self.ui.lineEdit_4.text()
        numdoc = self.ui.lineEdit_5.text()
        numtel = self.ui.lineEdit_6.text()

        gender = self.ui.box_gender.item

        data = [surname, name, familia, grajdanstwo, numdoc, numtel]
        self.savedatadb.saveperson(data)

    def backmenu(self):
        buywindow.close()
        userwindow.show()

        # ___________Окно возврата билета___________#



class ReturnTicket(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_vozv_tic()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.backmenu)

    def backmenu(self):
        returnticket.close()
        userwindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    userwindow = UserMain()
    revenuewin = Revenue()
    buywindow = BuyTicket()
    returnticket = ReturnTicket()
    userwindow.show()
    sys.exit(app.exec())
