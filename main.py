from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from PySide6.QtCore import Qt
import events
import re
import sys

class BirthdayTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dzimšanas dienu kalendārs")
        self.setGeometry(100, 100, 600, 400)  # x, y, width, height

        # Create the tab widget
        tab_control = QTabWidget()
        display_tab = QWidget()
        add_tab = QWidget()

        # Add tabs
        tab_control.addTab(display_tab, "Display")
        tab_control.addTab(add_tab, "Add Birthday")

        self.setCentralWidget(tab_control)

        # Display tab layout
        display_layout = QVBoxLayout()
        self.listbox = QListWidget()
        display_layout.addWidget(QLabel("This is the display tab"))
        display_layout.addWidget(self.listbox)
        display_tab.setLayout(display_layout)

        # Populate listbox
        for row in events.load_birthdays():
            self.listbox.addItem(''.join(row))

        # Add tab layout
        add_layout = QVBoxLayout()
        add_layout.addWidget(QLabel("This is the add tab"))

        # Name
        self.name_entry = QLineEdit()
        add_layout.addWidget(QLabel("Person's Name:"))
        add_layout.addWidget(self.name_entry)

        # Birthday
        self.birthday_entry = QLineEdit()
        add_layout.addWidget(QLabel("Birthday (YYYY/MM/DD):"))
        add_layout.addWidget(self.birthday_entry)

        # Add button
        add_button = QPushButton("Add Birthday")
        add_button.clicked.connect(self.add_birthday)
        add_layout.addWidget(add_button)

        add_tab.setLayout(add_layout)

    def add_birthday(self):
        name = self.name_entry.text()
        birthday = self.birthday_entry.text()
        birthday = birthday.replace('/', '-')
        birthday = birthday.strip()

        if not re.match(r'^\d{4}-\d{2}-\d{2}$', birthday):
            QMessageBox.critical(self, "Error", "Invalid date!")
            return

        events.save_birthday(name, birthday)
        QMessageBox.information(self, "Success", "Birthday added successfully!")
        self.listbox.addItem(f"{name} - {birthday}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = BirthdayTracker()
    mainWin.show()
    sys.exit(app.exec())
