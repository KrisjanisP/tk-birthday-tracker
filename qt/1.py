from PySide6.QtWidgets import QWidget, QApplication, QPushButton

app = QApplication([])

win = QWidget()
win.show()

win2 = QPushButton("TEST")
win2.show()

app.exec()