import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import ctypes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reprise")
        self.label = QLabel("Type a sequence", self)
        self.label.setGeometry(97,20,105,35)
        self.setFixedSize(300,200)
        self.editText = QTextEdit(self)
        self.editText.setGeometry(135,95,30,30)
        self.button = QPushButton("Start!", self)
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setGeometry(120,60,60,30)

        def update():
            time = self.timeEdit.time()
            value = time.toPyTime().hour * 3600 + time.toPyTime().minute * 60
            return value

        def verifyText():
            if(len(self.editText.toPlainText()) != 1):
                dialog = QDialog()
                dialog.setFixedSize(190,100)
                label = QLabel("Please type a one character", dialog)
                label.setGeometry(0,0,190,90)
                label.setMargin(10)
                dialog.exec_(str(update()))
            else:
                ctypes.windll.shell32.ShellExecuteW(
                    None,
                    u"runas",
                    u"python3.exe",
                    u"" + os.path.abspath("./Keyboard.py") + " " + self.editText.toPlainText() + " " + str(update()),
                    None,
                    1
                )

        self.button.setGeometry(115,140,70,30)
        self.button.clicked.connect(verifyText)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
