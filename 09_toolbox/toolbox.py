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






app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
