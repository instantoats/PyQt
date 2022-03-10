# Form implementation generated from reading ui file 'radiodemo.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(648, 534)
        Dialog.setStyleSheet("QLabel {\n"
"color: purple\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 200, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(90, 370, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 90, 72, 86))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonPython = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonPython.setFont(font)
        self.radioButtonPython.setObjectName("radioButtonPython")
        self.radioButtonPython.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.radioButtonPython)
        self.radioButtonJava = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonJava.setFont(font)
        self.radioButtonJava.setObjectName("radioButtonJava")
        self.radioButtonJava.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.radioButtonJava)
        self.radioButtonJS = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonJS.setFont(font)
        self.radioButtonJS.setObjectName("radioButtonJS")
        self.radioButtonJS.toggled.connect(self.radio_selected)

        self.verticalLayout.addWidget(self.radioButtonJS)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 240, 106, 56))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonPaypal = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonPaypal.setFont(font)
        self.radioButtonPaypal.setObjectName("radioButtonPaypal")
        self.radioButtonPaypal.toggled.connect(self.radio_selected)


        self.verticalLayout_2.addWidget(self.radioButtonPaypal)
        self.radioButtonCredit = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonCredit.setFont(font)
        self.radioButtonCredit.setObjectName("radioButtonCredit")

        # signal connection
        self.radioButtonCredit.toggled.connect(self.radio_selected)

        self.verticalLayout_2.addWidget(self.radioButtonCredit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radio_selected(self):
        selected1 = ""
        selected2 = ""

        if self.radioButtonPython.isChecked() == True:
            selected1 = "Python"
        if self.radioButtonJava.isChecked() == True:
            selected1 = "Java"
        if self.radioButtonJS.isChecked() == True:
            selected1 = "JavaScript"

        if self.radioButtonCredit.isChecked() == True:
            selected2 = "Credit/Debit Card"
        if self.radioButtonPaypal.isChecked() == True:
            selected2 = "Paypal"

        self.label_result.setText("Chosen Book " + selected1 + " |  Chosen Payment Method " + selected2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose your book"))
        self.label_2.setText(_translate("Dialog", "Choose your payment method"))
        self.radioButtonPython.setText(_translate("Dialog", "Python"))
        self.radioButtonJava.setText(_translate("Dialog", "Java"))
        self.radioButtonJS.setText(_translate("Dialog", "JS"))
        self.radioButtonPaypal.setText(_translate("Dialog", "Paypal"))
        self.radioButtonCredit.setText(_translate("Dialog", "Credit/debit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
