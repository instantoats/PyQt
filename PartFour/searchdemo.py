from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_dbname = QtWidgets.QLineEdit(Form)
        self.lineEdit_dbname.setObjectName("lineEdit_dbname")
        self.horizontalLayout_3.addWidget(self.lineEdit_dbname)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_tblname = QtWidgets.QLineEdit(Form)
        self.lineEdit_tblname.setObjectName("lineEdit_tblname")
        self.horizontalLayout_2.addWidget(self.lineEdit_tblname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)

        # connect signal
        self.pushButton.clicked.connect(self.search_data)

        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_4.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def search_data(self):
        dbname = self.lineEdit_dbname.text()
        try:

            mydb = mc.connect(
            host="localhost",
            user="root",
            password="pass",
            database=dbname
            )

            query = "SELECT password FROM " + self.lineEdit_tblname.text() + " where username like'" + self.lineEdit_username.text() + "'"
            mycursor = mydb.cursor()
            mycursor.execute(query)

            row = mycursor.fetchone()

            if row == None:
                self.label_result.setText("No user found with this username")
                self.lineEdit_password.setText("")

            else:
                self.label_result.setText("Username found")
                self.lineEdit_password.setText(row[0])
        except mc.Error as e:
            self.label_result.setText("Error in connection")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database Name: "))
        self.label_2.setText(_translate("Form", "Table Name:"))
        self.label_3.setText(_translate("Form", "Username: "))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_4.setText(_translate("Form", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
