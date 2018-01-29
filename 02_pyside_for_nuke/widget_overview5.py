from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        layout = QHBoxLayout()
        layout2 = QHBoxLayout()

        for i in range(4):
            layout.addWidget(QCheckBox())

        for i in range(4):
            layout2.addWidget(QLineEdit())

        master_layout = QVBoxLayout()
        master_layout.addLayout(layout)
        master_layout.addLayout(layout2)

        self.setLayout(master_layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
