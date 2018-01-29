from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()

        line = QLineEdit("My test")
        # line.setText("My Text")
        print line.text()
        line.setReadOnly(False)
        line.setMaxLength(10)
        # line.setEchoMode(QLineEdit.Password)
        line.setAlignment(Qt.AlignCenter)

        l = ["welcome", "hello", "world"]
        completer = QCompleter(l)
        line.setCompleter(completer)
        line.setPlaceholderText("Enter your name here..")

        push = QPushButton("Push")
        push.setText("New Push")
        push.setIcon(QIcon("nuke.png"))
        push.setShortcut("u")
        push.setToolTip("This is a tooltip!")
        push.setCheckable(True)

        checkbox = QCheckBox("Checkbox")
        checkbox.setChecked(True)
        print checkbox.isChecked()

        combo = QComboBox()
        combo.addItem("Hello")
        combo.addItems(["World", "test", "test2"])
        print combo.currentText()
        print combo.currentIndex()
        index = combo.findText("test")
        print index
        combo.setCurrentIndex(index)

        label = QLabel("Label")

        layout = QHBoxLayout()
        layout.addWidget(line)
        layout.addWidget(push)
        layout.addWidget(checkbox)
        layout.addWidget(combo)
        layout.addWidget(label)
        self.setLayout(layout)

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
