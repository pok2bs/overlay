from import_pyside6 import *
from gui.custom_button import *
from gui.custom_line_edit import *

class MainWindow(object):
    def set_ui(self, parent):
        self.central_widget = QWidget()
        
        #왼쪽
        self.left_layout = QVBoxLayout()
        self.label = QLabel("사용자 설정")
        self.set_short_cut_button = AppButton("단축키")
        self.set_short_cut_button.add_style("text-align: left; padding: 5px")
        self.set_window_button = AppButton("창")
        self.set_window_button.add_style("text-align: left; padding: 5px;")

        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding )

        self.close_button = AppButton(text="종료", color= "FF5050", hover= "FF9090", pressed= "FF0000")
        self.close_button.setMaximumWidth(200)
        self.close_button.setMinimumWidth(200)
        
        self.left_layout.addWidget(self.label)
        self.left_layout.addWidget(self.set_short_cut_button)
        self.left_layout.addWidget(self.set_window_button)
        self.left_layout.addItem(vertical_spacer)
        self.left_layout.addWidget(self.close_button)

        #오른쪽
        self.right_layout = QVBoxLayout()
        self.name_label = QLabel("<b>설정</b>")
        self.name_label.setFont(QFont("맑은 고딕", 20))
        self.name_label.setMinimumWidth(300)

        self.set_area = QStackedLayout()
        self.right_layout.addWidget(self.name_label)
        self.right_layout.addLayout(self.set_area)

        #단축키 설정
        self.short_cut_frame = QFrame()
        self.short_cut_layout = QHBoxLayout()
        self.short_cut_line = DefaltLineEdit()
        self.short_cut_line.setPlaceholderText("단축키를 입력하세요")
        self.short_cut_button = AppButton("적용")

        self.short_cut_layout.addWidget(self.short_cut_line)
        self.short_cut_layout.addWidget(self.short_cut_button)
        self.short_cut_layout.setAlignment(Qt.AlignTop)

        self.short_cut_frame.setLayout(self.short_cut_layout)

        self.set_area.addWidget(self.short_cut_frame)
        self.set_area.setCurrentWidget(self.short_cut_frame)
        self.name_label.setText("단축키")

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)

        self.central_widget.setLayout(self.main_layout)
        parent.setCentralWidget(self.central_widget)