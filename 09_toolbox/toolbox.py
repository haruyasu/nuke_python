from PySide.QtGui import *
from PySide.QtCore import *
import os
import json
import sys

HOME_FOLDER = os.path.join(os.path.expanduser("~"), ".nuke")

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.resize(400, 400)
        mouse_positon = QCursor.pos()
        self.move(mouse_positon - QPoint(200, 200))
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_QuitOnClose)

        self.selected_item = None

        self.mouse_destination = QPoint(self.width()/2, self.height()/2)

        self.layout = QGridLayout()
        self.layout.addWidget(ActionLabel(1), 0, 0)
        self.layout.addWidget(ActionLabel(2), 0, 1)
        self.layout.addWidget(ActionLabel(3), 0, 2)
        self.layout.addWidget(ActionLabel(4), 1, 0)
        self.layout.addWidget(ActionLabel(5), 1, 2)
        self.layout.addWidget(ActionLabel(6), 2, 0)
        self.layout.addWidget(ActionLabel(7), 2, 1)
        self.layout.addWidget(ActionLabel(8), 2, 2)

        self.setLayout(self.layout)

        action_path = os.path.join(HOME_FOLDER, "actions")
        if not os.path.exists(action_path):
            os.makedirs(action_path)

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return
        if event.text() == "n":
            if self.selected_item is None:
                self.close()
                return
            exec self.selected_item.code
            self.close()

    def paintEvent(self, QPaintEvent):
        super(Panel, self).paintEvent(QPaintEvent)
        painter = QPainter(self)

        self.draw_line(painter)
        self.set_label_color()

        nuke_image = QPixmap("%s/nuke.png" % HOME_FOLDER)
        painter.drawPixmap(QPoint(self.width()/2-24, self.height()/2-24), nuke_image)

    def set_label_color(self):
        widgets = [self.layout.itemAt(i).widget() for i in range(self.layout.count())]
        self.selected_item = None
        for w in widgets:
            if self.line.intersected(w.geometry()):
                w.set_selected(True)
                self.selected_item = w
            else:
                w.set_selected(False)

    def draw_line(self, painter):
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        center = QPoint(self.width() / 2, self.height() / 2)
        destination = self.mouse_destination
        self.line = QPolygon([center, center + QPoint(1, 0), destination, destination + QPoint(-1, 0)])
        painter.drawPolygon(self.line)

    def mouseMoveEvent(self, event):
        self.mouse_destination = event.pos()
        self.update()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
class Dialog(QDialog):
    def __init__(self, id):
        super(Dialog, self).__init__()

        self.id = id
        self.action_path = os.path.join(HOME_FOLDER, "actions", "%s.txt" % self.id)
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        self.code_plain_text = QPlainTextEdit()

        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_line_edit)

        master_layout = QVBoxLayout()
        master_layout.addWidget(name_layout)
        master_layout.addWidget(self.code_plain_text)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        master_layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        self.setLayout(master_layout)
        self.load_action()

    def load_action(self):
        if os.path.exists(self.action_path):
            doc = json.load(open(self.action_path))
            name = doc["name"]
            code = doc["code"]
            self.name_line_edit.setText(name)
            self.code_plain_text.setPlainText(code)

    def save_action(self):
        doc = dict()
        doc["name"] = self.name_line_edit.text()
        doc["code"] = self.code_plain_text.toPlainText()
        path = open(self.action_path, "w")
        json.dump(doc, path)

class ActionLabel(QLabel):
    def __init__(self, id):
        super(ActionLabel, self).__init__()

        self.id = id
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking(True)
        self.setFixedWidth(100)
        self.setFixedHeight(25)
        self.setStyleSheet("""background:red;
                            color:black""")
        self.set_action()

    def set_action(self):
        path = os.path.join(HOME_FOLDER, "actions", "%s.txt" % self.id)
        print path
        if os.path.exists(path):
            doc = json.load(open(path))
            name = doc["name"]
            code = doc["code"]
        else:
            name = "Action %s" % self.id
            code = ""

        self.setText(name)
        self.code = code

    def mousePressEvent(self, event):
        if event.buttons() == Qt.RightButton:
            dialog = Dialog(self.id)
            if dialog.exec_():
                dialog.save_action()
            self.parent().close()

    def set_selected(self, is_selected):
        if is_selected:
            self.setStyleSheet("""background:green;
                                    color:black""")
        else:
            self.setStyleSheet("""background:red;
                                    color:black""")

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
