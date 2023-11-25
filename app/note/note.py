import PySide6.QtGui
from import_pyside6 import *
from gui.app_base import OverlayWindow
import sys

class NoteWindow(OverlayWindow):
    def __init__(self, parent):
        super().__init__()

        self.text_edit = QTextEdit()
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.setContentsMargins(10,10,10,10)

        main_frame = QFrame()
        main_frame.setStyleSheet("background-color: #404040; color: white; border-radius: 15px;")
        main_frame.setLayout(main_layout)

        self.setCentralWidget(main_frame)
        self.resize(700, 400)

        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.open_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.save_as_shortcut = QShortcut(QKeySequence("Ctrl+S+A"), self)
        self.font_size_shortcut = QShortcut(QKeySequence("Ctrl+]"), self)
        self.font_minus_size_shortcut = QShortcut(QKeySequence("Ctrl+["), self)


        self.shortcut.activated.connect(self.save)
        self.open_shortcut.activated.connect(self.open)
        self.save_as_shortcut.activated.connect(self.save_as)
        self.font_size_shortcut.activated.connect(self.font_plus)
        self.font_minus_size_shortcut.activated.connect(self.font_minus)

        self.setWindowTitle("메모장")

        self.font_size = 10
        self.text_edit.setFont(QFont('맑은 고딕', self.font_size))
        self.nomal = False
        self.parent = parent
        
    def change_show(self):
        if self.nomal:
            self.hide()
            self.nomal = False
        else:
            self.showNormal()
            self.nomal = True
        pass

    def save_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", r"C/", ".txt", "html")
        if path == '':
            return
        self.path = path + _

        with open(self.path, "w", encoding="utf-8") as save: 
            save.write(self.text_edit.toPlainText())
            
    def save(self):
        if not "path" in dir(self):
            path, _ = QFileDialog.getSaveFileName(self, "Save File", r"C/", ".txt")
            if path == '':
                return
            self.path = path + _

        with open(self.path, "w", encoding="utf-8") as save: 
            save.write(self.text_edit.toPlainText())

    def font_plus(self):
        self.font_size += 1
        self.text_edit.setFont(QFont('맑은 고딕', self.font_size))

    def font_minus(self):
        self.font_size -= 1
        self.text_edit.setFont(QFont('맑은 고딕', self.font_size))

    def open(self):
        path, _ = QFileDialog.getOpenFileName(self, ".txt")
        if path == "":
            return
        self.path = path
        with open(path, "rt", encoding="utf-8") as save: 
            self.text_edit.setText(save.read())

    def closeEvent(self, event: QCloseEvent) -> None:
        self.parent.note.remove(self)
        return super().closeEvent(event)
