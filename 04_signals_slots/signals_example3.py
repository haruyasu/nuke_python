from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        self.label = QLabel("Click me...")
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        position = event.pos()
        x, y = position.x(), position.y()
        self.label.setText("The mouse position is x:%s y:%s" % (x, y))


app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
