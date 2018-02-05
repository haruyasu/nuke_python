from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.resize(500, 500)
        self.origin = None
        self.destination = None
        self.lines = []

    def paintEvent(self, QPaintEvent):
        super(Panel, self).paintEvent(QPaintEvent)

        painter = QPainter(self)
        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(5)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing)

        for line in self.lines:
            painter.drawLine(line)

        if self.destination:
            line = QLine(self.origin, self.destination)
            painter.drawLine(line)

    def mousePressEvent(self, event):
        self.origin = event.pos()

    def mouseMoveEvent(self, event):
        self.destination = event.pos()
        self.lines.append(QLine(self.origin, self.destination))
        self.origin = event.pos()
        self.update()


app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
