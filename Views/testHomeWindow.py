# Form implementation generated from reading ui file '.\Views\testHomeWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Controllers.Cabinet_Controller import *
from Views.stateCabinet import Ui_outpInformationWindow


class Ui_TestHomeWindow(object):
    def setupUi(self, TestHomeWindow):
        TestHomeWindow.setObjectName("TestHomeWindow")
        TestHomeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=TestHomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        # ########################################################

        ####################################################################
        self.toolButtoCabinet = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButtoCabinet.setGeometry(QtCore.QRect(40, 180, 281, 71))
        self.toolButtoCabinet.setObjectName("toolButtoCabinet")
        TestHomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=TestHomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        TestHomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=TestHomeWindow)
        self.statusbar.setObjectName("statusbar")
        TestHomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TestHomeWindow)
        QtCore.QMetaObject.connectSlotsByName(TestHomeWindow)

    def retranslateUi(self, TestHomeWindow):
        _translate = QtCore.QCoreApplication.translate
        TestHomeWindow.setWindowTitle(_translate("TestHomeWindow", "MainWindow"))
        # self.radioButtonCabinet.setText(_translate("TestHomeWindow", "Выберите кабинет"))
        self.toolButtoCabinet.setText(_translate("TestHomeWindow", "Перейти в окно Стостояние кабинета"))

    def radio_button(self):
        cab_y = 100
        cab = Cabinet_Controller()
        self.list_radiobutton = []
        for cabinet in cab.get():
            # name_button = f"radioButtonCabinet_{cabinet.id}"
            # self.name = f"radioButtonCabinet{cabinet.id}"
            self.name = QtWidgets.QRadioButton(f'{cabinet.id}',parent=self.centralwidget)
            self.name.cabinet = cabinet.name
            self.name.setGeometry(QtCore.QRect(500, cab_y, 201, 21))
            # self.name.setObjectName(name_button)
            _translate = QtCore.QCoreApplication.translate
            self.name.setText(_translate("TestHomeWindow", f"Выберите кабинет номер {cabinet.name}"))
            self.list_radiobutton.append(self.name)
            cab_y += 23
    def onClicked(self):
        for button in self.list_radiobutton:
            if button.isChecked():
                cabinet_name = button.cabinet
        global outpInformationWindow
        # 4 скопированы из stateCABINET
        outpInformationWindow = QtWidgets.QMainWindow()
        ui = Ui_outpInformationWindow(cabinet_name)
        ui.setupUi(outpInformationWindow)
        def test():
            print('!!!!!')
            ui.show_state_lamps()
        ui.pushButtonAll.clicked.connect(test)
        outpInformationWindow.show()









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestHomeWindow = QtWidgets.QMainWindow()
    ui = Ui_TestHomeWindow()
    ui.setupUi(TestHomeWindow)
    ui.radio_button()
    # print(ui.list_radiobutton)
    sys._excepthook = sys.excepthook


    def my_exeption_hook(exctype, value, traceback):
        print(exctype, value, traceback)

        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = my_exeption_hook

    try:
        sys.exit(app.exec_())

    except:

        ui.toolButtoCabinet.clicked.connect(ui.onClicked)

    TestHomeWindow.show()
    sys.exit(app.exec())
