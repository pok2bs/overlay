from import_pyside6 import *
from app.image.viewer import ViewWindow

class ViewerManager(QObject):
    def __init__(self, parent):
        super().__init__()
        parent.showed.connect(self.show)
        parent.hid.connect(self.hide)

        self.view = list()
        self.parent = parent
    
    def new_window(self, from_browser = False):
        view = ViewWindow(self)
        if not from_browser:
            view.openCall()
            view.show()
            self.view.append(view)
        else:
            view.set_clipboard_img()

            view.show()
            if self.parent.isHidden():
                view.title_bar.toggle_button.click()
                view.set_no_overlay()
            self.view.append(view)

    def show(self):
        for view in self.view:
            view.set_overlay()

    def hide(self):
        for view in self.view:
            view.set_no_overlay()
