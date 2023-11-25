import PySide6.QtWidgets
from import_pyside6 import *
from gui.custom_button import defaltButton
# 출처 https://stackoverflow.com/questions/62807295/how-to-resize-a-window-from-the-edges-after-adding-the-property-qtcore-qt-framel
class SideGrip(QWidget):
    def __init__(self, parent, edge):
        QWidget.__init__(self, parent)
        if edge == Qt.LeftEdge:
            self.setCursor(Qt.SizeHorCursor)
            self.resizeFunc = self.resizeLeft
        elif edge == Qt.TopEdge:
            self.setCursor(Qt.SizeVerCursor)
            self.resizeFunc = self.resizeTop
        elif edge == Qt.RightEdge:
            self.setCursor(Qt.SizeHorCursor)
            self.resizeFunc = self.resizeRight
        else:
            self.setCursor(Qt.SizeVerCursor)
            self.resizeFunc = self.resizeBottom
        self.mousePos = None

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None


class Main(QMainWindow):
    _gripSize = 6
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.bg = '#000000'
        self.opacity = 0.01


        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Tool |
            Qt.WindowStaysOnTopHint)

        self.sideGrips = [
            SideGrip(self, Qt.LeftEdge), 
            SideGrip(self, Qt.TopEdge), 
            SideGrip(self, Qt.RightEdge), 
            SideGrip(self, Qt.BottomEdge), 
        ]
        # corner grips should be "on top" of everything, otherwise the side grips
        # will take precedence on mouse events, so we are adding them *after*;
        # alternatively, widget.raise_() can be used
        self.cornerGrips = [QSizeGrip(self) for i in range(4)]

    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(*[self.gripSize] * 4)

        outRect = self.rect()
        # an "inner" rect used for reference to set the geometries of size grips
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
            -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QRect(outRect.topLeft(), inRect.topLeft()))
        # top right
        self.cornerGrips[1].setGeometry(
            QRect(outRect.topRight(), inRect.topRight()).normalized())
        # bottom right
        self.cornerGrips[2].setGeometry(
            QRect(inRect.bottomRight(), outRect.bottomRight()))
        # bottom left
        self.cornerGrips[3].setGeometry(
            QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())
        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)
        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(), 
            inRect.top(), self.gripSize, inRect.height())
        # bottom edge
        self.sideGrips[3].setGeometry(
            self.gripSize, inRect.top() + inRect.height(), 
            inRect.width(), self.gripSize)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        self.updateGrips()


    def paintEvent(self, event=None):
        painter = QPainter(self)
        painter.setOpacity(self.opacity)
        painter.setBrush(QColor(self.bg))
        painter.setPen(QPen(QColor(0,0,0)))   
        painter.drawRect(self.rect())

    def setCentralWidget(self, widget: QWidget) -> None:
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(CustomTitleBar(self))
        main_layout.addWidget(widget)
        main_layout.setContentsMargins(0,0,0,0)
        main_widget.setLayout(main_layout)
        return super().setCentralWidget(main_widget)

class CustomTitleBar(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.setMaximumHeight(25)
        self.setMinimumHeight(25)

        self.setStyleSheet("background-color:#A0A0A0; border-radius:10px; opacity:0.7")
        self.parent = parent
        
        self.max_button = defaltButton("ㅁ")
        self.mini_button = defaltButton("_")
        self.close_button = defaltButton("X")
        horizen_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum )



        self.main_layout = QHBoxLayout()
        self.main_layout.addItem(horizen_spacer)

        self.main_layout.addWidget(self.mini_button)
        self.main_layout.addWidget(self.max_button)
        self.main_layout.addWidget(self.close_button)
        self.main_layout.setContentsMargins(0,0,10,0)

        self.setLayout(self.main_layout)



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # self.clickPos = event.windowPos().toPoint()
            self.clickPos = event.scenePosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            # self.window().move(event.globalPos() - self.clickPos)
            self.parent.window().move(event.globalPosition().toPoint() - self.clickPos)