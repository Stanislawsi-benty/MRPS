from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 40, 600, 320))
        self.listView.setObjectName("listView")
        self.btn_buy_tic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buy_tic.setGeometry(QtCore.QRect(370, 380, 200, 40))
        self.btn_buy_tic.setIconSize(QtCore.QSize(20, 20))
        self.btn_buy_tic.setObjectName("btn_buy_tic")
        self.btn_vozv_tic = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vozv_tic.setGeometry(QtCore.QRect(70, 380, 200, 40))
        self.btn_vozv_tic.setIconSize(QtCore.QSize(20, 20))
        self.btn_vozv_tic.setObjectName("btn_vozv_tic")
        self.btn_go_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go_back.setGeometry(QtCore.QRect(220, 440, 200, 40))
        self.btn_go_back.setIconSize(QtCore.QSize(20, 20))
        self.btn_go_back.setObjectName("btn_go_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 600, 40))
        self.label.setWordWrap(False)
        self.label.setIndent(6)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_buy_tic.setText(_translate("MainWindow", "Купить билет"))
        self.btn_vozv_tic.setText(_translate("MainWindow", "Вернуть билет"))
        self.label.setText(_translate("MainWindow", "Список рейсов"))
        self.btn_go_back.setText(_translate("MainWindow", "Идентификация"))
