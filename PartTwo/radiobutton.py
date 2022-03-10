from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("PyQt6 QRadioButton")
        self.setWindowIcon(QIcon('images/rando.png'))

        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()

        rad1 = QRadioButton("That Biz Person")
        rad1.setIcon(QIcon("images/bus_icon1.png"))
        rad1.setIconSize(QSize(40, 40))
        rad1.setFont(QFont("Times", 14))
        #default this button as checked
        rad1.setChecked(True)
        rad1.toggled.connect(self.radio_selected)

        rad2 = QRadioButton("This Biz Person")
        rad2.setIcon(QIcon("images/bus_icon2.png"))
        rad2.setIconSize(QSize(40, 40))
        rad2.setFont(QFont("Times", 14))
        rad2.toggled.connect(self.radio_selected)

        rad3 = QRadioButton("The Biz Person")
        rad3.setIcon(QIcon("images/bus_icon3.png"))
        rad3.setIconSize(QSize(40, 40))
        rad3.setFont(QFont("Times", 14))
        rad3.toggled.connect(self.radio_selected)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        hbox.addWidget(rad3)

        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText("You have selected : {} ".format(radio_btn.text()))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())