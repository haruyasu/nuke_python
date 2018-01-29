from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        line1 = QLineEdit()
        line2 = QLineEdit()
        # line3 = QLineEdit()
        line4 = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(line1, 25)
        layout.addSpacing(25)
        layout.addWidget(line2, 25)
        # layout.addWidget(line3, 1)
        layout.addStretch(25)
        layout.addWidget(line4, 100)

        self.setLayout(layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
