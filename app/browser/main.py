from import_pyside6 import *
from app.browser.browser import BrowserWindow
import json, sys 

class BrowserManager(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.hover = True
        self.view = list()
        self.profile = QWebEngineProfile()
        self.save_path = self.profile.defaultProfile().persistentStoragePath().rstrip("OffTheRecord")
        print(type(self.profile))
        self.update()        
        
        self.close_num = 0
        self.delete_path_list = list()
        parent.showed.connect(self.show)
        parent.hid.connect(self.hide)
    def show(self):
        for view in self.view:
            view.set_overlay()

    def hide(self):
        for view in self.view:
            view.set_no_overlay()
                
            
    def load(self):
        try:
            with open(f"{self.save_path}save.json","r") as save:
                self.profile_list = json.load(save)

        except:
            self.profile_list = list()
            with open(f"{self.save_path}save.json","w",encoding="utf-8") as save:
                json.dump(self.profile_list, save, indent="\t")

    @Slot(int, int)
    def update(self, num = None, del_num = None):
        self.load()
        
        for view in self.view:
            view.profile_list = self.profile_list
            if not view.profile_num is None and num == view.profile_num: 
                view.bookmarks_update(del_num)

    @Slot(QWebEngineProfile)
    def new_window(self, profile):
        view = BrowserWindow(self)
        self.profile = profile
        try:
            storage_name = self.profile.persistentStoragePath().split("/")[-1].lstrip("storage-")
        except:
            self.profile = QWebEngineProfile().defaultProfile()
            storage_name = "OffTheRecord"
            print("error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        view.ui.view_widget.setPage(QWebEnginePage(self.profile, view.ui.view_widget))
        view.new_profile_window.connect(self.new_window)
        view.saved.connect(self.update)
        
        self.view.append(view)
        
        if storage_name != "OffTheRecord":
            view.profile_num = int(storage_name) - 1
            print(storage_name)
            self.load()
            view.bookmarks_update()
        else:
            view.signal_connect()
        view.ui.view_widget.setUrl(QUrl("https:/www.google.com"))
        
        if self.parent.isHidden():
            view.title_bar.toggle_button.click()
            view.set_no_overlay()

        view.show()

        return view.ui.view_widget
    
    @Slot(QWebEngineProfile, QUrl)
    def new_url_window(self, profile, url):
        self.new_window(profile).setUrl(url)

    def appCloseEvent(self):
        print("close")
        for view in self.view:
            view.deleteLater()
