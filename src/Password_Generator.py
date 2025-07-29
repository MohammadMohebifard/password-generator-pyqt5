import sys
import random
import string
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QCheckBox, QSpinBox, QMessageBox 
)
from PyQt5.QtGui import QFont

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(200, 200, 320, 360)
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        layout = QVBoxLayout()

        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Generated password appears here")
        layout.addWidget(self.password_display)

        self.length_input = QSpinBox()
        self.length_input.setRange(4, 20)
        self.length_input.setValue(8)
        layout.addWidget(QLabel("Password Length:"))
        layout.addWidget(self.length_input)

        self.upper = QCheckBox("Include Uppercase (A-Z)")
        self.upper.setChecked(True)
        self.lower = QCheckBox("Include Lowercase (a-z)")
        self.lower.setChecked(True)
        self.digits = QCheckBox("Include Digits (0-9)")
        self.digits.setChecked(True)
        self.symbols = QCheckBox("Include Symbols (!@#$...)")
        self.symbols.setChecked(True)

        layout.addWidget(self.upper)
        layout.addWidget(self.lower)
        layout.addWidget(self.digits)
        layout.addWidget(self.symbols)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_password)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def apply_styles(self):
        self.setFont(QFont("Tahoma", 10))

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
            }

            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                padding: 8px;
                font-size: 14px;
                border-radius: 6px;
            }

            QLabel {
                font-weight: bold;
                color: #333333;
                margin-top: 10px;
            }

            QCheckBox {
                font-size: 13px;
                color: #444444;
            }

            QSpinBox {
                padding: 5px;
                font-size: 13px;
            }

            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px;
                margin-top: 5px;
            }

            QPushButton:hover {
                background-color: #27ae60;
            }
        """)

    def generate_password(self):
        chars = ""
        if self.upper.isChecked():
            chars += string.ascii_uppercase
        if self.lower.isChecked():
            chars += string.ascii_lowercase
        if self.digits.isChecked():
            chars += string.digits
        if self.symbols.isChecked():
            chars += string.punctuation

        if not chars:
            self.password_display.setText("Please select at least one option")
            return

        length = self.length_input.value()
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_display.setText(password)

    def copy_password(self):
        password = self.password_display.text()
        if password:
            QApplication.clipboard().setText(password)
            QMessageBox.information(self, "Copied", "Password copied to clipboard!")
        else:
            QMessageBox.warning(self, "Warning", "No password to copy!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
