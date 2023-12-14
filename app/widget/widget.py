import PySide6.QtCore
from import_pyside6 import *
from gui.custom_button import AppButton
from gui.custom_line_edit import DefaltLineEdit
from app.browser.browser import BrowserWindow

class Widget(QWidget):
    hover = Signal(bool)
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.setWindowFlags(
            Qt.Tool |
            Qt.FramelessWindowHint |
            Qt.CustomizeWindowHint |
            Qt.X11BypassWindowManagerHint |
            Qt.WindowStaysOnTopHint
                        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.main_frame = QFrame()
        
        self.hover = False

        self.line = DefaltLineEdit(color=202020, hover=404040, pressed= "000000", size_x= 40, size_y= 40, radius= 20)
        self.line.setMinimumWidth(400)
        self.search_Button = AppButton(text = "검색", size_x= 40, size_y= 40, radius= 20)
        self.note_Button = AppButton(text = "메모장", size_x= 40, size_y= 40, radius= 20)
        self.browser_Button = AppButton(text= "브라우저",size_x= 40, size_y= 40, radius= 20)
        self.image_Button = AppButton(text="이미지", size_x= 40, size_y= 40, radius= 20)
        self.more_Button = AppButton(text= "...", size_x= 40, size_y= 40, radius= 20)
        self.size_Button = AppButton(text= "-", size_x= 40, size_y= 40, radius= 20)

        self.search_Button.setMaximumSize(self.size_Button.minimumSize())
        self.note_Button.setMaximumSize(self.size_Button.minimumSize())
        self.browser_Button.setMaximumSize(self.size_Button.minimumSize())
        self.image_Button.setMaximumSize(self.size_Button.minimumSize())
        self.more_Button.setMaximumSize(self.size_Button.minimumSize())
        self.size_Button.setMaximumSize(self.size_Button.minimumSize())

        self.note_Button.clicked.connect(self.parent.note.new_window)
        self.browser_Button.clicked.connect(self.parent.browser.new_window)
        self.image_Button.clicked.connect(self.parent.view.new_window)

        self.more_Button.clicked.connect(self.button_display_change)
        self.more = False
        self.button_display_change()

        self.main_frame.setStyleSheet("background-color:#353535; border-radius: 25px")
        self.main_frame.setMinimumSize(0,0)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.line)
        self.main_layout.addWidget(self.search_Button)
        self.main_layout.addWidget(self.note_Button)
        self.main_layout.addWidget(self.browser_Button)
        self.main_layout.addWidget(self.image_Button)
        self.main_layout.addWidget(self.more_Button)
        self.main_layout.addWidget(self.size_Button)

        self.main_layout.setSpacing(self.main_layout.contentsMargins().left())

        self.parent.showed.connect(self.activateWindow)
        self.profile_list = list()

        self.view = BrowserWindow(self)
        self.view.title_bar.hide()
        self.view._gripSize = 0
        self.view.setMinimumHeight(400)
        self.line.returnPressed.connect(self.set_url)

        self.main_frame.setLayout(self.main_layout)
        layout = QVBoxLayout()
        layout.addWidget(self.main_frame)
        layout.addWidget(self.view)

        self.setLayout(layout)
        self.transform()
        self.size_Button.clicked.connect(self.transform)
        self.search_Button.clicked.connect(self.transform)

    def new_window(self, profile):
        return self.parent.browser.new_window(profile)

    def transform(self):
        if self.size_Button.isHidden():

            self.size_Button.show()
            self.search_Button.hide()
            self.line.show()
            self.line.setFocus()
            self.resize(500, 100)
        else:
            self.line.hide()
            self.search_Button.show()
            self.view.setMinimumWidth(0)
            self.size_Button.hide()
            self.setMinimumSize(0,0)
            self.setMaximumSize(0,0)
            self.view.hide()
            print(self.main_layout.spacing())

            self.resize(0,0)


        print(self.size())



    def signal_raley(self):
        self.parent.view.new_window(True)
    
    def set_url(self):
        self.view.setMinimumWidth(self.width())

        self.view.move_to_url(self.line.text())
        self.view._gripSize = 0
        self.view.show()

        print(self.parent)

    def button_display_change(self):
        if self.more:
            self.note_Button.hide()
            self.image_Button.hide()
            self.browser_Button.hide()
            self.more = False
            self.setMinimumSize(0,0)
            self.setMaximumSize(0,0)
            self.resize(500, 100)
        else:
            self.note_Button.show()
            self.image_Button.show()
            self.browser_Button.show()
            self.more = True

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setWindowOpacity(1)

    
    def leaveEvent(self, event: QEnterEvent) -> None:
        if not self.search_Button.isHidden():
            self.setWindowOpacity(0.6)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # self.clickPos = event.windowPos().toPoint()
            self.clickPos = event.scenePosition().toPoint()
        print("click")

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            # self.window().move(event.globalPos() - self.clickPos)
            self.window().move(event.globalPosition().toPoint() - self.clickPos)

