import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        label = QLabel("Hello Nuke!!")
        layout = QHBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

def start():
    start.panel = Panel()
    start.panel.show()
