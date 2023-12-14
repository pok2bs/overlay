# 단축키 모듈, Pyside6, MainUi 불러오기

from pynput.keyboard import Key, KeyCode, GlobalHotKeys
from import_pyside6 import *
from gui.main_ui import MainUi
from app.browser.main import BrowserManager
from app.note.main import NoteManager
from app.image.main import ViewerManager
from app.widget.widget import Widget
from app.setting.setting import SettingWindow

import sys, threading

event = threading.Event()
thread_run = False
class main(MainUi):
    def __init__(self):
        super().__init__()
        
        self.browser = BrowserManager(self)
        self.note = NoteManager(self)
        self.view = ViewerManager(self)
        self.hover = False
        
        self.task_bar.browser_Button.clicked.connect(lambda : self.browser.new_window(QWebEngineProfile().defaultProfile()))
        self.task_bar.note_Button.clicked.connect(self.note.new_window)
        self.task_bar.setting_Button.clicked.connect(self.setting_change)
        self.task_bar.widget_Button.clicked.connect(self.widget_change)
        self.task_bar.image_Button.clicked.connect(self.view.new_window)

        self.hot_key = GlobalHotKeys({"<ctrl>+d": self.change_show})
        self.hot_key.start() 

    def widget_change(self):
        if not "widget" in dir(self):
            self.widget = Widget(self)
        if self.widget.isHidden():
            self.widget.show()
        else:
            self.widget.close()

    def setting_change(self):
        if not "setting" in dir(self):
            self.setting = SettingWindow(self)

        self.setting.ui.close_button.clicked.connect(self.close)

        self.setting.show()

    def change_show(self):
        if not self.isHidden():
            self.hide()
            self.hid.emit()
        else:
            self.showFullScreen()
            self.showed.emit()

    def hot_key_change(self, key):
        self.hot_key.stop()
        self.hot_key = GlobalHotKeys({key: self.change_show})       
        self.hot_key.start()

    def enterEvent(self, event: QEnterEvent) -> None:
        self.hover = True
        
    def leaveEvent(self, event: QEnterEvent) -> None:
        self.hover = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print("click")

        if self.hover:
            self.change_show()
        return super().mousePressEvent(event)
    
    def closeEvent(self, event: QCloseEvent):
        self.browser.appCloseEvent()
        self.browser.deleteLater()

        self.note.deleteLater()

        self.setting.close()
        self.setting.deleteLater()
        
        self.task_bar.close()
        self.task_bar.deleteLater()

        self.deleteLater()
        self.hot_key.stop()

        event.accept() 

if __name__ == "__main__":
        app = QApplication(sys.argv)
        app_main = main()
        app_main.change_show()
        app.exec()
    




