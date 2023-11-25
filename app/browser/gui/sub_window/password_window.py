from import_pyside6 import *
from gui.app_base import OverlayWindow
from gui.custom_line_edit import *
from gui.custom_button import *

class password_widget(OverlayWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.Tool |
            Qt.WindowStaysOnTopHint |
            Qt.X11BypassWindowManagerHint |
            Qt.FramelessWindowHint
            )
        self.password_layout = QVBoxLayout()
        self.profile_name = QLabel()
        self.profile_name.setAlignment(Qt.AlignCenter)
        self.profile_password_line = DefaltLineEdit()
        self.profile_password_line.setPlaceholderText("비밀번호")
        self.profile_password_line.setEchoMode(DefaltLineEdit.Password)
        self.password_error = QLabel()
        self.password_error.setStyleSheet("color:rad")

        self.accept_button = AppButton("확인")
        self.is_new_window_show = QCheckBox("새 창에서 열기")

        self.password_layout.addWidget(self.profile_name)
        self.password_layout.addWidget(self.profile_password_line)
        self.password_layout.addWidget(self.password_error)
        self.password_layout.addWidget(self.is_new_window_show)
        self.password_layout.addWidget(self.accept_button)
        self.password_layout.setSpacing(10)
        self.password_layout.setContentsMargins(10,20,10,20)

        main_frame = QFrame()
        main_frame.setStyleSheet("background-color: #404040; color: white; border-radius: 15px;")

        main_frame.setLayout(self.password_layout)
        self.setCentralWidget(main_frame)
        self.setWindowTitle("비밀번호")