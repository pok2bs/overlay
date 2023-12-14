import PySide6.QtGui
from import_pyside6 import *
from gui.app_base import OverlayWindow
#from PIL import ImageGrab, BmpImagePlugin, Image
import io, time, requests, clipboard, base64
from binascii import a2b_base64

class ViewWindow(OverlayWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.label = QLabel(self)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setAlignment(Qt.AlignCenter)
        self.label.setContentsMargins(0,0,0,0)

        # Create new action
        self.open_shortcut = QShortcut(QKeySequence("Ctrl+O"), self)

        self.open_shortcut.activated.connect(self.openCall)

        # Create menu bar and add action
        self.setCentralWidget(self.scroll_area)
        self.main_layout.setContentsMargins(0,0,0,0)

        self.scroll_area.setStyleSheet("background-color:black; border:0px")
        self.resize(600, 600)

    def set_clipboard_img(self):
        #time.sleep(0.5)
        #img_byte = io.BytesIO()
        #img = ImageGrab.grabclipboard()
        # 출처 https://stackoverflow.com/questions/34697559/pil-image-to-qpixmap-conversion-issue
        #if type(img) != None:
            
            #img = img.convert("RGB")
            #data = img.tobytes("raw", "RGB")
            #self.img = QImage(data, img.size[0], img.size[1], img.size[0]*3, QImage.Format.Format_RGB888)
            #self.pixmap = QPixmap.fromImage(self.img)
        session = requests.Session()
        while True:
            QApplication.processEvents()
            try:
                self.url = clipboard.paste()
            except:
                pass
            if "url" in dir(self):
                break
        print(self.url)
        if QUrl(self.url).scheme() == "https" or QUrl(self.url).scheme() == "http":
            respone = session.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            data = respone.content
        else:
            #출처 https://stackoverflow.com/questions/33870538/how-to-parse-data-uri-in-python
            header, encoded = self.url.split("base64,", 1)
            data = base64.b64decode(encoded)
        self.setWindowTitle("웹 이미지")
        self.img = data

    def openCall(self):
        path, _ = QFileDialog.getOpenFileName(self, ".*")
        with open(path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            
        self.setWindowTitle("이미지 - " + path.split("/")[-1])

        self.img = bytes(b)
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.img)
        self.pixmap = self.pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())


    def resizeEvent(self, event):
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.img)
        self.pixmap = self.pixmap.scaled(self.width()- 15, self.height() - self.title_bar.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        return super().resizeEvent(event)

    def set_no_overlay(self):
        if self.title_bar.toggle_button.is_active:
            self.resize(self.pixmap.width(), self.pixmap.height())

        return super().set_no_overlay()
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.parent.view.remove(self)
        event.accept()
        return super().closeEvent(event)

