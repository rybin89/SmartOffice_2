import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Views.cameras import Ui_camerasWindow
from Views.editCamera import Ui_editCameraWindow

app = QtWidgets.QApplication(sys.argv)
camerasWindow = QtWidgets.QMainWindow()
cameras = Ui_camerasWindow()
ui = Ui_editCameraWindow()
ui.clicked_button
cameras.setupUi(camerasWindow)

camerasWindow.show()

def open_edit_cameras():
    # global MainWindow
    MainWindow = QtWidgets.QMainWindow()

    ui.setupUi(MainWindow)
    # ui.clicked_button()
    camerasWindow.close()
    MainWindow.show()
    def open_cameras():
        MainWindow.close()
        camerasWindow.show()

    ui.infotButton.clicked.connect(open_cameras)


cameras.infotButton.clicked.connect(open_edit_cameras)
sys.exit(app.exec())




