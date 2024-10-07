from PyQt6.QtWidgets import (
    QApplication,
    QStackedWidget,
    QPushButton,
    QHBoxLayout, QWidget
)
from smartOff import *



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