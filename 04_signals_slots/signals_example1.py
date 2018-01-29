from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        # push = QPushButton("Close")
        # push.clicked.connect(self.close)

        self.line = QLineEdit()
        self.line2 = QLineEdit()

        self.line.textChanged.connect(self.line_edit_cout)

        layout = QHBoxLayout()
        # layout.addWidget(push)
        layout.addWidget(self.line)
        layout.addWidget(self.line2)
        self.setLayout(layout)

    def line_edit_cout(self):
        text = self.line.text()
        count = len(text)
        self.line2.setText(str(count))

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
