from PySide.QtGui import *
from PySide.QtCore import *
import os
import json
import sys

HOME_FOLDER = os.path.join(os.path.expanduser("~"), ".nuke")

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.resize(400, 400)
        mouse_positon = QCursor.pos()
        self.move(mouse_positon - QPoint(200, 200))
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_QuitOnClose)

        self.selected_item = None

        self.mouse_destination = QPoint(self.width()/2, self.height()/2)

        self.layout = QGridLayout()
        self.layout.addWidget(ActionLabel(1), 0, 0)
        self.layout.addWidget(ActionLabel(2), 0, 1)
        self.layout.addWidget(ActionLabel(3), 0, 2)
        self.layout.addWidget(ActionLabel(4), 1, 0)
        self.layout.addWidget(ActionLabel(5), 1, 2)
        self.layout.addWidget(ActionLabel(6), 2, 0)
        self.layout.addWidget(ActionLabel(7), 2, 1)
        self.layout.addWidget(ActionLabel(8), 2, 2)

        self.setLayout(self.layout)

        action_path = os.path.join(HOME_FOLDER, "actions")
        if not os.path.exists(action_path):
            os.makedirs(action_path)

    def keyReleaseEvent(self, event):
        pass





app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
