from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        line1 = QLineEdit()
        line2 = QLineEdit()
        line3 = QLineEdit()
        line4 = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(line1, 0, 0)
        layout.addWidget(line2, 1, 0)
        layout.addWidget(line3, 0, 1)
        layout.addWidget(line4, 1, 1)

        self.setLayout(layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
