# Form implementation generated from reading ui file '.\Vews\CabinetView.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Controllers.Cabinet_Controller import *
import sys
class Ui_MainWindow(object):
    cabinet = Cabinet_Controller()
    label_y = 40
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 775)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(100, 560, 341, 71))
        self.startButton.setStyleSheet("background-color: rgb(167, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(220, 208, 115);")
        self.startButton.setObjectName("startButton")

        self.labelDepartament1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelDepartament1.setGeometry(QtCore.QRect(540, 560, 401, 61))
        self.labelDepartament1.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
                                            "background-color: rgb(41, 125, 0);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "padding:5px;\n"
                                            "border-radius:10px;")
        self.labelDepartament1.setObjectName("labelDepartament")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        self.cabinets_show()
        self.department_show()


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelDepartament1.setText(_translate("MainWindow", "TextLabel"))
        self.startButton.setText(_translate("MainWindow", "PushButton"))


    def cabinets_show(self):

        for cab in self.cabinet.get():

            self.labelCabinet = QtWidgets.QLabel(parent=self.centralwidget)
            self.labelCabinet.setGeometry(QtCore.QRect(80, self.label_y, 401, 61))
            self.labelCabinet.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
                                            "background-color: rgb(57, 0, 172);\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "padding:5px;\n"
                                            "border-radius:10px;")
            self.labelCabinet.setObjectName("labelCabinet")
            self.label_y += 110
            _translate = QtCore.QCoreApplication.translate
            self.labelCabinet.setText(_translate("MainWindow", cab.name))

    def department_show(self):
        label_y = 40
        for cab in self.cabinet.get():

            self.labelDepartament = QtWidgets.QLabel(parent=self.centralwidget)
            self.labelDepartament.setGeometry(QtCore.QRect(540, label_y, 401, 61))
            self.labelDepartament.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
                                                "background-color: rgb(41, 125, 0);\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "padding:5px;\n"
                                                "border-radius:10px;")
            self.labelDepartament.setObjectName("labelDepartament")
            label_y +=110
            _translate = QtCore.QCoreApplication.translate
            self.labelDepartament.setText(_translate("MainWindow",  cab.department))
    def on_click(self):

        self.labelDepartament1.setText(str(self.cabinet.count_filds()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)



    ui.startButton.clicked.connect(ui.on_click)
    print(type(ui.cabinet.count_filds()))
    MainWindow.show()
    sys.exit(app.exec())

print('WEDADDA')