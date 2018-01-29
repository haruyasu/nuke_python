from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        layout = QHBoxLayout()
        self.checkbox1 = QCheckBox("Checkbox 1")
        self.checkbox2 = QCheckBox("Checkbox 2")
        self.checkbox3 = QCheckBox("Checkbox 3")
        self.checkbox4 = QCheckBox("Checkbox 4")
        self.checkbox5 = QCheckBox("Checkbox 5")

        self.checkbox1.clicked.connect(self.who_clicked)
        self.checkbox2.clicked.connect(self.who_clicked)
        self.checkbox3.clicked.connect(self.who_clicked)
        self.checkbox4.clicked.connect(self.who_clicked)
        self.checkbox5.clicked.connect(self.who_clicked)

        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)
        layout.addWidget(self.checkbox4)
        layout.addWidget(self.checkbox5)

        self.line = QLineEdit()
        layout.addWidget(self.line)

        self.setLayout(layout)

    def who_clicked(self):
        sender = self.sender()
        label = sender.text()
        self.line.setText(label)

        l = [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4, self.checkbox5]
        for i in l:
            if i == sender:
                i.setChecked(True)
            else:
                i.setChecked(False)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
