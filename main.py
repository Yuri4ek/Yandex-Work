import sys
import io

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import QPointF, QRectF, Qt
from random import randint

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def random_seat(self):
        x = randint(100, 700)
        y = randint(100, 500)
        return QPointF(x, y)

    def random_selected_color(self):
        color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        return QColor(color[0], color[1], color[2])

    def drawer(self, qp):
        size = randint(20, 100)
        qp.setBrush(self.random_selected_color())
        qp.setPen(QColor(0, 0, 0))

        qp.drawEllipse(self.random_seat(), size, size)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawer(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
