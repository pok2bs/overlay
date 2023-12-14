from app.setting.gui.main_window import MainWindow 
from gui.app_base import *

class SettingWindow(OverlayWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = MainWindow()
        self.ui.set_ui(self)
        self.resize(600, 400)

        self.ui.short_cut_button.clicked.connect(lambda x:parent.hot_key_change(self.ui.short_cut_line.text()))

        parent.hid.connect(self.hide)
        parent.showed.connect(self.show)

        self.setWindowTitle("설정")