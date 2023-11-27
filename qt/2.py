from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QSize

class BirthdayTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("birthday tracker")
        self.setMinimumSize(QSize(300,200))

        button = QPushButton("hello")
        button.clicked.connect(self.pushed_button)

        self.setCentralWidget(button)
    
    def pushed_button(self):
        print("button clicked")

app = QApplication()

win = BirthdayTracker()
win.show()

app.exec()