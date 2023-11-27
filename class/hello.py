from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

app = QApplication([])

window = QWidget()
window.show()

test = QPushButton("Test")
test.show()

main = QMainWindow()
main.show()

app.exec()
