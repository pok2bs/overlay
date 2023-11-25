from import_pyside6 import *


        
class defaltButton(QPushButton):
    def __init__(self, text: str(), hover = 606060, color = 404040, pressed= 202020):
        super().__init__()
        self.setText(text)
        self.setFont(QFont("맑은 고딕", 8))
        self.setStyleSheet(f'''QPushButton{{
                           color: white;
                           background-color: #{color};
                           border-radius: 15px
        }}
                           
                              QPushButton::hover{{
                           background-color:#{hover};
                              }}
                              QPushButton::pressed{{
                           background-color:#{pressed}
                              }}''')
        
class taskBarButton(defaltButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setMinimumWidth(50)
        self.setMinimumHeight(50)
        self.setMaximumWidth(50)
        self.setFont(QFont("맑은 고딕", 8))
        self.setStyleSheet('''QPushButton{
                           color: white;
                           background-color: #404040;
                           border-radius: 15px
        } 
                           
                              QPushButton::hover{
                           background-color:#606060;
                              }
                              QPushButton::pressed{
                           background-color:#202020
                              }''')
        