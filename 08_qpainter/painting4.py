from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.color = QColor(255, 0, 0)
        self.origin = None
        self.destination = None

    def paintEvent(self, QPaintEvent):
        super(Panel, self).paintEvent(QPaintEvent)

        painter = QPainter(self)
        brush = QBrush(self.color)
        painter.setBrush(brush)
        rect = QRect(100, 100, 200, 200)
        painter.drawRect(rect)

        if not self.destination:
            return

        point1 = self.origin
        point2 = self.origin + QPoint(10, 0)
        point3 = self.destination
        point4 = self.destination + QPoint(-10, 0)

        poly = QPolygon([point1, point2, point3, point4])
        painter.drawPolygon(poly)

        if poly.intersected(rect):
            print "intersected"

    def mousePressEvent(self, event):
        self.origin = event.pos()

    def mouseMoveEvent(self, event):
        self.destination = event.pos()
        self.update()

app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
