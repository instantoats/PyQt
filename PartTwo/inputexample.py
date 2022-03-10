from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QDialog, QLineEdit, QInputDialog, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QInputExample")
        self.setWindowIcon(QIcon('images/rando.png'))

        self.create_dialog()

    def create_dialog(self):
        hbox = QHBoxLayout()

        label = QLabel("Choose country:")
        label.setFont(QFont("Times", 15))

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont("Times", 15))

        btn = QPushButton("Choose country")
        btn.setFont(QFont("Times", 15))
        btn.clicked.connect(self.get_int)

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(btn)

        self.setLayout(hbox)

    def show_dialog(self):
        countries = [
            "Afghanistan", "Albania", "Canada", "Pakistan"
        ]

        country, ok = QInputDialog.getItem(self, "Input Dialog", "List of countries", countries, 0, False)

        if ok and country:
            self.lineedit.setText(country)

    def get_text(self):
        mytext, ok = QInputDialog.getText(self, "Get Username", "Enter your name : ")
        if ok and mytext:
            self.lineedit.setText(mytext)

    def get_int(self):
        mynumber, ok = QInputDialog.getInt(self, "Order Quantity", "Enter Quantity : ", 1, 2, 30, 50)

        if ok and mynumber:
            self.lineedit.setText(str(mynumber))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())