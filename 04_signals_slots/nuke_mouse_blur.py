from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

    def mouseMoveEvent(self, event):
        b = nuke.createNode("Blur", inpanel=False)
        b.setXYpos(event.pos().x(), event.pos().y())

p = Panel()
p.show()
