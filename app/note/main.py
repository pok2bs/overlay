from import_pyside6 import *
from app.note.note import NoteWindow

class NoteManager(QObject):
    def __init__(self, parent):
        super().__init__()
        parent.showed.connect(self.show)
        parent.hid.connect(self.hide)

        self.note = list()
    
    def new_window(self):
        note = NoteWindow(self)
        note.show()
        self.note.append(note)

    def show(self):
        for note in self.note:
            note.show()

    def hide(self):
        for note in self.note:
            note.hide()


