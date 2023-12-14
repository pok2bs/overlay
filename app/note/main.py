from import_pyside6 import *
from app.note.note import NoteWindow

class NoteManager(QObject):
    def __init__(self, parent):
        super().__init__()
        parent.showed.connect(self.show)
        parent.hid.connect(self.hide)
        self.parent = parent

        self.note = list()
    
    def new_window(self):
        note = NoteWindow(self)
        if self.parent.isHidden():
            note.title_bar.toggle_button.click()
            note.set_no_overlay()
        note.show()
        self.note.append(note)

    def show(self):
        for note in self.note:
            note.set_overlay()

    def hide(self):
        for note in self.note:
            note.set_no_overlay()

