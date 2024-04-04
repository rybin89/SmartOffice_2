from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QStackedWidget,
    QPushButton,
    QLabel,
    QHBoxLayout, QWidget
)
from PyQt6 import QtCore
from PyQt6 import QtGui
from Views.stateCabinet import *
from Views.smartOff import *



app = QApplication([])
stacked_widget = QStackedWidget()
window_one = Ui_MainWindow()
window_two = Ui_outpInformationWindow()
stacked_widget.addWidget(window_one)
stacked_widget.addWidget(window_two)
button = QPushButton("Switch Window")
stacked_widget.setCurrentIndex(0)
layout = QHBoxLayout()
layout.addWidget(button)
layout.addWidget(stacked_widget)
window = QWidget()
window.setLayout(layout)
window.show()
app.exec_()