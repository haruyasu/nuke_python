from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        super(Panel, self).paintEvent(QPaintEvent)

        painter = QPainter(self)
        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(5)
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)

        line = QLine(QPoint(0, 0), QPoint(self.width(), self.height()))
        painter.drawLine(line)

        image = QPixmap("nuke.png").scaled(200, 200)
        painter.drawPixmap(QPoint(200, 200), image)

        # pen2 = QPen(QColor(0, 255, 0))
        # pen2.setWidth(2)
        # painter.setPen(pen2)
        painter.setPen(Qt.NoPen)

        brush = QBrush(QColor(0, 0, 255))
        brush.setStyle(Qt.DiagCrossPattern)
        painter.setBrush(brush)

        rectangle = QRect(25, 50, 100, 200)
        painter.drawRect(rectangle)


app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
