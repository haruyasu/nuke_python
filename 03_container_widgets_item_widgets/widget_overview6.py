from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        group1 = QGroupBox("Checkbox")
        group1.setEnabled(False)
        group1_layout = QHBoxLayout()
        for i in range(5):
            c = QCheckBox()
            group1_layout.addWidget(c)
        group1.setLayout(group1_layout)

        group2 = QGroupBox("Line edit")
        group2_layout = QHBoxLayout()
        for i in range(5):
            line = QLineEdit()
            group2_layout.addWidget(line)
        group2.setLayout(group2_layout)

        master_layout = QVBoxLayout()
        master_layout.addWidget(group1)
        master_layout.addWidget(group2)
        self.setLayout(master_layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
