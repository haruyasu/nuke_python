from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        table = QTabWidget()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        for i in range(5):
            layout1.addWidget(QPushButton())

        for i in range(5):
            layout2.addWidget(QCheckBox())

        for i in range(5):
            layout3.addWidget(QLineEdit())

        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)
        tab3.setLayout(layout3)

        table.addTab(tab1, "Push", )
        table.addTab(tab2, "Checkbox")
        table.addTab(tab3, "Line Edit")

        master_layout = QHBoxLayout()
        master_layout.addWidget(table)
        self.setLayout(master_layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
