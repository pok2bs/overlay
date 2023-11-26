import PySide6.QtGui
from import_pyside6 import *
from gui.custom_button import TaskBarButton

class taskBar(QWidget):
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
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.main_frame = QFrame()
        
        self.main_frame.setMaximumHeight(75)
        self.hover = False

        self.note_Button = TaskBarButton("메모장")
        self.browser_Button = TaskBarButton("브라우저")
        self.image_Button = TaskBarButton("이미지")
        self.music_Button = TaskBarButton("음악")

        self.main_frame.setStyleSheet("background-color:#353535; border-radius: 20px")

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

        self.main_frame.setLayout(self.main_layout)
        layout = QVBoxLayout()
        layout.addWidget(self.main_frame)
        self.setLayout(layout)

    def window_move(self):
        self.move(self.parent.width()/3 + self.width()/2,self.parent.height() - 100 - self.height())
        self.activateWindow()
        self.show()

    def enterEvent(self, event: QEnterEvent) -> None:
        self.hover = True
    
    def leaveEvent(self, event: QEnterEvent) -> None:
        self.hover = False
    

        
