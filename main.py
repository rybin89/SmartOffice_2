from Vews.CabinetView import *
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
# ui.setupUi(MainWindow)








ui.startButton.clicked.connect(ui.on_click)
MainWindow.show()
sys.exit(app.exec())