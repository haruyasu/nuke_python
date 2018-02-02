from PySide.QtGui import *
from PySide.QtCore import *
from clipboardUi import ClipboardUi
import sys

class ClipboardCore(ClipboardUi):
    def __init__(self):
        super(ClipboardCore, self).__init__()

app = QApplication(sys.argv)
panel = ClipboardCore()
panel.show()
app.exec_()
