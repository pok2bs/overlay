
from import_pyside6 import *

class Clock(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("시계")
        self.initWidgets()
	            
        self.setWindowFlags(
        Qt.Tool |
        Qt.FramelessWindowHint |
        Qt.WindowStaysOnTopHint
        )
        self.parent.showed.connect(self.show)
        self.parent.hid.connect(self.hide)
        self.hover = False



    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.mouseClick = True
            self.oldPos = e.globalPos()

    def mouseReleaseEvent(self, e):
        self.mouseClick = False

    def mouseMoveEvent(self, e):
        if self.mouseClick:
            delta = QPoint (e.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = e.globalPos()

    def initWidgets(self):
        self.layout = QVBoxLayout()
        self.day_label = QLabel()
        self.day_label.setAlignment(Qt.AlignCenter)
        self.day_label.setFrameStyle(QFrame.NoFrame)
        self.day_label.setFont(QFont("맑은 고딕", 10))
        self.day_label.setStyleSheet("color:white")

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFrameStyle(QFrame.NoFrame)
        self.time_label.setFont(QFont("맑은 고딕", 50))
        self.time_label.setStyleSheet("color:white")

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.show_time()
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.day_label)
        self.setLayout(self.layout)

    def show_time(self):
        time = QTime.currentTime()
        day = QDate.currentDate()
        self.currentTime = time.toString('hh:mm')
        locale = QLocale(QLocale.Korean)
        self.day = locale.toString(day, 'MM월 dd일 dddd')

        self.day_label.setText(f"<b>{self.day}</b>")
        self.time_label.setText(f"<b>{self.currentTime}</b>")

    def mousePressEvent(self, event: QMouseEvent) -> None:

        return super().mousePressEvent(event)
