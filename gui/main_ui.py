from import_pyside6 import *
from gui.time_widget import Clock
from gui.task_bar import taskBar

import sys, math

class MainUi(QWidget):
    showed = Signal()
    hid = Signal()
    def __init__(self):
        super().__init__()

        self.clock = Clock(self)
        self.task_bar = taskBar(self)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout = QVBoxLayout(self)
        
        self.main_layout.addWidget(self.clock)
        self.main_layout.addItem(verticalSpacer)
        self.main_layout.setContentsMargins(0,0,0,100)

        self.setLayout(self.main_layout)

        self.setWindowFlags(
            Qt.Tool |
            Qt.FramelessWindowHint |
            Qt.CustomizeWindowHint |
            Qt.X11BypassWindowManagerHint |
            Qt.WindowStaysOnTopHint
                        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.nomal = False

    def paintEvent(self, e):
        
        qp = QPainter()
        qp.begin(self)
        qp.setOpacity(0.5)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(0,0,0))
        qp.setPen(QPen(QColor(0,0,0), 3))
        qp.drawRect(self.geometry())


        