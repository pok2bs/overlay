import PySide6.QtGui
from import_pyside6 import *
from gui.custom_button import taskBarButton

class taskBar(QFrame):
    hover = Signal(bool)
    def __init__(self, parent):
        super().__init__()
        self.setWindowFlags(
            Qt.Tool |
            Qt.FramelessWindowHint |
            Qt.CustomizeWindowHint |
            Qt.X11BypassWindowManagerHint |
            Qt.WindowStaysOnTopHint
                        )
        self.setMaximumHeight(75)
        self.hover = False

        self.note_Button = taskBarButton("메모장")
        self.browser_Button = taskBarButton("브라우저")
        self.image_Button = taskBarButton("이미지")
        self.music_Button = taskBarButton("음악")

        self.setStyleSheet("background-color:#353535; border-radius: 15px")

        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.note_Button)
        self.main_layout.addWidget(self.browser_Button)
        self.main_layout.addWidget(self.image_Button)
        self.main_layout.addWidget(self.music_Button)
        self.main_layout.setSpacing(self.main_layout.contentsMargins().left())

        self.setMaximumSize(self.main_layout.minimumSize())
        self.parent = parent
        self.parent.showed.connect(self.window_move)
        self.parent.hid.connect(self.hide)

        self.setLayout(self.main_layout)

    def window_move(self):
        self.move(self.parent.width()/3 + self.width()/2,self.parent.height() - 100 - self.height())
        self.activateWindow()
        self.show()

    def enterEvent(self, event: QEnterEvent) -> None:
        self.hover = True
    
    def leaveEvent(self, event: QEnterEvent) -> None:
        self.hover = False
    

        