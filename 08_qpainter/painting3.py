from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.color = QColor(255, 0, 0)

    def paintEvent(self, QPaintEvent):
        super(Panel, self).paintEvent(QPaintEvent)

        painter = QPainter(self)
        brush = QBrush(self.color)
        painter.setBrush(brush)
        self.rect = QRect(100, 100, 200, 200)
        painter.drawRect(self.rect)

    def mousePressEvent(self, event):
        pos = event.pos()
        if self.rect.contains(pos):
            self.color = QColor(Qt.green)
        else:
            self.color = QColor(Qt.red)
        self.update()



app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
