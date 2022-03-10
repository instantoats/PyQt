from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
from NotePadDemo import Ui_MainWindow


class NotePadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


        self.actionSave.triggered.connect(self.save_file)


    def save_file(self):
        filename = QFileDialog.getSaveFileName(self, "Save File")

        if filename[0]:
            f = open(filename[0], 'w')

        with f:
            text = self.textEdit.toPlainText()
            f.write(text)

        QMessageBox.about(self, "Save File", "File has been saved")


app = QApplication(sys.argv)
Note = NotePadWindow()
sys.exit(app.exec())


