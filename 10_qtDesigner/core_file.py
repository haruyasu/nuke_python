from PySide.QtGui import *
from PySide.QtCore import *
from interface import Ui_Form

class Panel(QWidget, Ui_Form):
    def __init__(self):
        super(Panel, self).__init__()
        self.setupUi(self)

        self.save_push_button.clicked.connect(self.set_name)

    def set_name(self):
        self.name_line_edit.setText("Hello World!!")

app = QApplication([])
panel = Panel()
panel.show()
app.exec_()
