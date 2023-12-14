from import_pyside6 import *
from bs4 import BeautifulSoup

class customWebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.set = False
    def contextMenuEvent(self, event):
        self.menu = self.createStandardContextMenu()

        self.menu.setStyleSheet("""
            QMenu{
                  background-color: #404040;
                  border-radius: 20px;
            }
            QMenu::item {
                    background-color: transparent;
                    color: white;
                    padding:3px 20px;
                    margin:5px 10px;
            }
            QMenu::item:selected { background-color: gray; border-radius: 20px;}
        """)
        for action in self.menu.actions():
            action.setText(self.context_translate(action.text()))
            if action.text() == "이미지 주소 복사" :
                img_copy = action
                open_img = QAction("이미지 열기")
                open_img.triggered.connect(lambda x: img_copy.trigger())

                if not self.set:
                    img_copy.triggered.connect(self.window().signal_raley)
                    self.set = True
                self.menu.insertAction(img_copy, open_img)
        self.menu.popup(event.globalPos())

    def callback_function(self, html):
        print(type(html))
        html_data = BeautifulSoup(html, 'html.parser') 
        program_names = html_data.text

    def get_text(self):
        self.page().runJavaScript("document.getElementsByTagName('html')[0].outerHTML", 0, self.callback_function)

    def context_translate(self, text):
            translate_list = [("Back", "뒤로"), ("Forward", "앞으로"), ("Reload", "새로고침"), 
                              ("Save image","이미지 저장"), ("Save page", "페이지 저장"), 
                              ("Copy image", "이미지 복사"), ("Copy image address", "이미지 주소 복사"), 
                              ("Copy link address", "링크 주소 복사"), ("Save link", "링크 저장"), 
                              ("Open link in new tab","링크 열기"), ("Open link in new window","새 창에서 링크 열기"),
                              ("View page source", "페이지 소스 보기"),
                              ("Copy", "복사"),("Paste", "붙여넣기"),("Cut", "자르기")]
            for i in range(0, len(translate_list)):
                 if text == translate_list[i][0]:
                      return translate_list[i][1]
            return text


    def createWindow(self, type_):

        if type_ == QWebEnginePage.WebBrowserWindow:

            return self.parent.parent.new_window(profile = self.parent.ui.view_widget.page().profile())
        if type_ == QWebEnginePage.WebBrowserTab:

            self.parent.background_view_widget = QWebEngineView()
            self.parent.background_view_widget.urlChanged.connect(self.parent.set_tab_url)
            self.parent.match_page = QWebEnginePage(self.parent.ui.view_widget.page().profile())
            self.parent.background_view_widget.setPage(self.parent.match_page)

            return self.parent.background_view_widget
        
        return QWebEngineView.createWindow(self, type_)
        