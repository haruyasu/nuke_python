from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        list_widget = QListWidget()
        # list_widget.addItem("Hello")
        # list_widget.addItems(["World", "test"])
        # list_widget.sortItems()

        items = ["World", "Test", "Python"]
        for item in items:
            i = QListWidgetItem(item)
            i.setToolTip("Hello Tooltios")
            i.setIcon(QIcon("nuke.png"))
            # i.setBackground(QColor(255, 175, 0))
            list_widget.addItem(i)
        list_widget.setAlternatingRowColors(True)
        list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        master_layout = QHBoxLayout()
        master_layout.addWidget(list_widget)
        self.setLayout(master_layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
