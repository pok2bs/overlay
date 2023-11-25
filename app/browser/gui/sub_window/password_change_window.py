from import_pyside6 import *
from gui.app_base import OverlayWindow
from gui.custom_line_edit import *
from gui.custom_button import *

class password_change_widget(OverlayWindow):
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
        self.profile_password_line.setPlaceholderText("현재 비밀번호")
        self.profile_password_line.setEchoMode(DefaltLineEdit.Password)
        self.password_error = QLabel()
        self.new_password_line = DefaltLineEdit()
        self.new_password_line.setPlaceholderText("새 비밀번호")
        self.new_password_line.setEchoMode(QLineEdit.Password)
        self.new_password_error = QLabel()
        self.new_password_check_line = DefaltLineEdit()
        self.new_password_check_line.setPlaceholderText("새 비밀번호 확인")
        self.new_password_check_line.setEchoMode(DefaltLineEdit.Password)
        self.new_password_check_error = QLabel()
        self.accept_button = AppButton("확인")
        self.password_layout.addWidget(self.profile_name)
        self.password_layout.addWidget(self.profile_password_line)
        self.password_layout.addWidget(self.password_error)
        self.password_layout.addWidget(self.new_password_line)
        self.password_layout.addWidget(self.new_password_error)
        self.password_layout.addWidget(self.new_password_check_line)
        self.password_layout.addWidget(self.new_password_check_error)
        self.password_layout.addWidget(self.accept_button)
        self.password_layout.setSpacing(10)
        self.password_layout.setContentsMargins(10,20,10,20)

        main_frame = QFrame()
        main_frame.setLayout(self.password_layout)
        self.setCentralWidget(main_frame)
        self.setWindowTitle("비밀번호")