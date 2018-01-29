from PySide.QtGui import *
from PySide.QtCore import *
import sys

class MyLineEdit(QLineEdit):
    def __init__(self):
        super(MyLineEdit, self).__init__()


class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        first_name_label = QLabel("First Name:")
        self.first_name = QLineEdit()
        self.first_name.setProperty("valid", False)
        self.first_name.setObjectName("first_name")
        last_name_label = QLabel("Last Name:")
        last_name = QLineEdit()
        name_layout = QHBoxLayout()
        name_layout.addWidget(first_name_label)
        name_layout.addWidget(self.first_name)
        name_layout.addWidget(last_name_label)
        name_layout.addWidget(last_name)

        role_label = QLabel("Role")
        role_combobox = QComboBox()
        role_combobox.addItems(["Pipeline TD", "Compositor", "FX TD", "Modeler", "Animator", "Lighting TD"])
        role_layout = QHBoxLayout()
        role_layout.addWidget(role_label)
        role_layout.addWidget(role_combobox)
        role_layout.addStretch()

        self.gender_male_checkbox = QCheckBox("male")
        self.gender_famale_checbox = QCheckBox("famale")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.gender_male_checkbox)
        gender_layout.addWidget(self.gender_famale_checbox)
        gender_layout.addStretch()

        list_widget = QListWidget()
        list_widget.addItems(["Canada", "USA", "Japan", "London", "Australia"])
        # list_widget.setAlternatingRowColors(True)

        save_push_button = QPushButton("OK")
        close_pusu_button = QPushButton("Close")
        action_layout = QHBoxLayout()
        action_layout.addWidget(save_push_button)
        action_layout.addWidget(close_pusu_button)

        master_layout = QVBoxLayout()
        master_layout.addLayout(name_layout)
        master_layout.addLayout(role_layout)
        master_layout.addLayout(gender_layout)
        master_layout.addWidget(list_widget)
        master_layout.addLayout(action_layout)

        self.setLayout(master_layout)

        # Signals
        close_pusu_button.clicked.connect(self.close)
        save_push_button.clicked.connect(self.show_message_box)
        self.gender_male_checkbox.clicked.connect(self.set_checkbox)
        self.gender_famale_checbox.clicked.connect(self.set_checkbox)
        self.first_name.textChanged.connect(self.check_validity)

        self.set_style_sheet()

    def check_validity(self, text):
        self.first_name.setProperty("valid", bool(text))
        self.set_style_sheet()

    def set_style_sheet(self):
        text = open("style.txt").read()
        self.setStyleSheet(text)

    def set_checkbox(self):
        self.gender_famale_checbox.setChecked(self.sender() is self.gender_famale_checbox)
        self.gender_male_checkbox.setChecked(self.sender() is self.gender_male_checkbox)

    def show_message_box(self):
        QMessageBox.information(self, "information", "User saved successfully!")

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
