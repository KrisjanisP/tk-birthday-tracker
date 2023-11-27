import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget
from PySide6.QtCore import QDate

class CalendarExample(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create Calendar Widget
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)

        # Connect the selectionChanged signal to a slot
        self.calendar.selectionChanged.connect(self.date_changed)

        # Set the window's main widget
        self.setCentralWidget(self.calendar)

    def date_changed(self):
        # This function is called when the user selects a date
        selected_date = self.calendar.selectedDate()
        print(f"Date selected: {selected_date.toString()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = CalendarExample()
    mainWin.show()
    sys.exit(app.exec())
