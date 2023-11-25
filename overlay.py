# 단축키 모듈, Pyside6, MainUi 불러오기

import PySide6.QtCore
import PySide6.QtGui
from pynput.keyboard import Key, KeyCode, GlobalHotKeys
from import_pyside6 import *
from gui.main_ui import MainUi
from app.browser.main import BrowserManager
from app.note.main import NoteManager

import win32api, sys, threading, json

class main(MainUi):
    def __init__(self):
        super().__init__()
        
        self.browser = BrowserManager(self)
        self.note = NoteManager(self)
        self.hover = False
        
        self.task_bar.browser_Button.clicked.connect(lambda : self.browser.new_window(QWebEngineProfile().defaultProfile()))
        self.task_bar.note_Button.clicked.connect(self.note.new_window)

    def change_show(self):
        if self.nomal:
            self.hide()
            self.hid.emit()
            self.nomal = False
        else:
            self.showFullScreen()
            self.showed.emit()
            self.nomal = True

    def enterEvent(self, event: QEnterEvent) -> None:
        self.hover = True
        
    def leaveEvent(self, event: QEnterEvent) -> None:
        self.hover = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        print("click")

        if self.hover:
            self.change_show()
        return super().mousePressEvent(event)

HOT_KEYS = {
    'execute': set([ Key.alt_l, KeyCode(char='1')] )
}
 
def execute():
    app_main.change_show()

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 A지정
    
    def run(self):
        with GlobalHotKeys({
                '<ctrl>+<alt>+d': execute}) as hot_key: hot_key.join()

name = "hot_key"
t = Worker(name)                # sub thread 생성
t.start() 

if __name__ == "__main__":
        app = QApplication(sys.argv)
        app_main = main()
        app_main.change_show()
        app.exec()

    




