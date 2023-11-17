import pathlib
from Air_db.conclusion_db import *
from Air_db.savedata_db import *
from pathlib import Path
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from Interfaces.mainWindow_User import Ui_MainWindow
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

    # открытие окна покупки билетов
    def activatebuy(self):
        userwindow.close()
        buywindow.show()

    # возврат в главное меню
    def returnticket(self):
        userwindow.close()
        returnticket.show()

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

        self.savedata_db = Save()

        self.ui.but_buy.clicked.connect(self.buyticket)
        self.ui.but_buy_2.clicked.connect(self.backmenu)

    #Сохрание данных в БД
    def buyticket(self):
        surname = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        familia = self.ui.lineEdit_3.text()
        grajdanstwo = self.ui.lineEdit_4.text()
        numdoc = self.ui.lineEdit_5.text()
        numtel = self.ui.lineEdit_6.text()

        data = [surname, name, familia, grajdanstwo, numdoc, numtel]
        self.savedata_db.savedata(data)

    # def good(self):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #
    #     msg.setText("Билет куплен, спасибо за покупку!!")
    #
    # def error(self):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #
    #     msg.setText("Введите данные коректно!!")

    #Возврат в главное меню
    def backmenu(self):
        buywindow.close()
        userwindow.show()


                                  #___________Окно возврата билета___________#
class ReturnTicket(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_vozv_tic()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.backmenu)

    #открытие окна возврата билетов
    def dopret(self):
        returnticket.close()
        dopreturn.show()

    # возврат в главное меню
    def backmenu(self):
        returnticket.close()
        userwindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    userwindow = UserMain()
    buywindow = BuyTicket()
    returnticket = ReturnTicket()
    userwindow.show()
    sys.exit(app.exec())
