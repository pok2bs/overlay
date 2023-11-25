from import_pyside6 import *
from gui.app_base import OverlayWindow
from gui.custom_line_edit import *
from gui.custom_button import *


class add_profile_widget(OverlayWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.Tool |
            Qt.WindowStaysOnTopHint |
            Qt.X11BypassWindowManagerHint |
            Qt.FramelessWindowHint
            )

        self.add_profile_layout = QVBoxLayout()
        self.profile_name_line = DefaltLineEdit()
        self.profile_name_line.setPlaceholderText("프로필 이름")
        self.profile_password_line = DefaltLineEdit()
        self.profile_password_line.setPlaceholderText("비밀번호")
        self.profile_password_line.setEchoMode(DefaltLineEdit.Password)
        self.accept_button = AppButton("확인")
        self.add_profile_layout.addWidget(self.profile_name_line)
        self.add_profile_layout.addWidget(self.profile_password_line)
        self.add_profile_layout.addWidget(self.accept_button)

        main_frame = QFrame()
        main_frame.setLayout(self.add_profile_layout)
        self.setCentralWidget(main_frame)

        self.setWindowTitle("프로필 추가")