from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        line = MyLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(line)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        print event.text()

class MyLineEdit(QLineEdit):
    def __init__(self):
        super(MyLineEdit, self).__init__()

    def enterEvent(self, event):
        self.setText("Mouse is in the Widget")

    def leaveEvent(self, event):
        self.setText("Mouse is outside the Widget")




app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
