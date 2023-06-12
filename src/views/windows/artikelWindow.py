from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json


class ArtikelWindow(QMainWindow):
    channel = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setUpArtikelWindow()

    def setUpArtikelWindow(self):
        self.resize(960, 600)

        # Get the size and position of the user's screen
        primary_screen = QGuiApplication.primaryScreen()
        screen = primary_screen.availableGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Center the window on the screen
        self.move(int((screen_width - self.width()) / 2),
                  int((screen_height - self.height()) / 2))

        # Assets path
        path = str(pathlib.Path(__file__).parent.absolute()) + \
            '/../../../assets/'

        # Fonts
        fonts_folder_path = path + 'fonts/'
        for filename in os.listdir(fonts_folder_path):
            if filename.endswith('.ttf') or filename.endswith('.otf'):
                font_path = os.path.join(fonts_folder_path, filename)
                QFontDatabase.addApplicationFont(font_path)

        self.setArtikel()
        self.initializeWidgets(path)

    def initializeWidgets(self, path):
        self.setStyleSheet('''
            *{
                border: none;
                background-color: transparent;
                background: transparent;
                padding: 0;
                margin: 0;
                font-family: Poppins;
            }

            #header {
                background-color: #3C6255;
            }

            #main {
                background-color: #F7F4D9;
            }

            #footer {
                background-color: #F7F4D9;
            }

            #btn_back {
                color: #F7F4D9;
                font-size: 20px;
                font-weight: 600;
            }

            #btn_back:hover {
                color: #DEDBC0;
            }

            #btn_prev, #btn_next {
                background-color: #61876E;
                border-radius: 25px;
            }

            #btn_prev:hover {
                background-color: #486E55;
            }

            #btn_next:hover {
                background-color: #486E55;
            }

            #label_title_artikel {
                color: #F7F4D9;
                background-color: #3C6255;
                padding: 15px 70px;
                border-radius: 25px;
                font-size: 28px;
                font-weight: 600;
            }

            #box_description_artikel {
                color: #F9F9F9;
                background-color: #3C6255;
                border-radius: 20px;
            }

            #text_description_artikel {
                color: #F7F4D9;
                padding: 0px 8px 10px;
                font-size: 14px;
                font-weight: 500;
            }

            #text_title_artikel {
                font-size: 18px;
                color: #F7F4D9;
                font-weight: 600;
                padding: 10px 8px 0px;
            }
            
            QScrollBar:vertical {
                border: none;
                width: 12px;
                margin: 8px 0px 8px 5px;
                border-radius: 0px;
            }
            
            /*  HANDLE BAR VERTICAL */
            QScrollBar::handle:vertical {    
                background-color: #F7F4D9;
                min-height: 20px;
                border-radius: 3px;
            }
            
            QScrollBar::handle:vertical:hover{    
                background-color: #23493C;
            }
            
            /* BTN TOP - SCROLLBAR */
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            /* BTN BOTTOM - SCROLLBAR */
            QScrollBar::add-line:vertical {
                height: 0px;
            }
            
            /* RESET ARROW */
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        ''')

        # Layouts
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Header
        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_temp = QtWidgets.QFrame(parent=self.header)
        self.frame_temp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp.setObjectName("frame_temp")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_temp)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_back = QtWidgets.QPushButton(parent=self.frame_temp)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path + "icons/left_arrow.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText(" Kembali")
        self.btn_back.setCursor(Qt.CursorShape.PointingHandCursor)

        self.horizontalLayout_3.addWidget(
            self.btn_back, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_temp)
        self.frame_logo = QtWidgets.QFrame(parent=self.header)
        self.frame_logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(parent=self.frame_logo)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setMaximumSize(QtCore.QSize(42, 42))
        self.logo.setPixmap(QtGui.QPixmap(path + "logo/logo_circle.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.frame_temp_2 = QtWidgets.QFrame(parent=self.header)
        self.frame_temp_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp_2.setObjectName("frame_temp_2")
        self.horizontalLayout.addWidget(self.frame_temp_2)
        self.verticalLayout.addWidget(self.header)

        # Main
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_title_artikel = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_artikel.setObjectName("label_title_artikel")
        self.label_title_artikel.setText("Artikel")

        self.horizontalLayout_4.addWidget(
            self.label_title_artikel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_contents_1 = QtWidgets.QFrame(parent=self.main)
        self.frame_contents_1.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_contents_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contents_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contents_1.setObjectName("frame_contents_1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_contents_1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        if (len(self.listArtikel) == 0):
            self.vertical_layout_x = QtWidgets.QVBoxLayout()
            self.vertical_layout_x.setContentsMargins(0, 90, 0, 0)
            self.vertical_layout_x.setSpacing(0)
            self.vertical_layout_x.setObjectName("vertical_layout_x")
            self.verticalLayout_2.addLayout(self.vertical_layout_x)

        self.frame_prev = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_prev.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_prev.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_prev.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_prev.setObjectName("frame_prev")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_prev)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 27, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Btn_Prev
        if (len(self.listArtikel) != 0):
            self.btn_prev = QtWidgets.QPushButton(parent=self.frame_prev)
            self.btn_prev.setMinimumSize(QtCore.QSize(50, 50))
            self.btn_prev.setMaximumSize(QtCore.QSize(50, 50))
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(path + "icons/left_arrow_circle.svg"),
                            QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btn_prev.setIcon(icon1)
            self.btn_prev.setIconSize(QtCore.QSize(26, 26))
            self.btn_prev.setObjectName("btn_prev")
            self.btn_prev.setCursor(Qt.CursorShape.PointingHandCursor)
            self.horizontalLayout_6.addWidget(self.btn_prev)
            
            self.btn_prev.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))

        self.horizontalLayout_5.addWidget(
            self.frame_prev, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.frame_img = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_img.setMinimumSize(QtCore.QSize(400, 190))
        self.frame_img.setMaximumSize(QtCore.QSize(400, 190))
        self.frame_img.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_img.setObjectName("frame_img")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.frame_img)
        self.hboxlayout.setObjectName("hboxlayout")
        self.widget_img = QtWidgets.QWidget(parent=self.frame_img)
        self.widget_img.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget_img.setObjectName("widget_img")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_img)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # if (len(self.listArtikel) != 0):
        # Stacked Widget
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_img)
        self.stackedWidget.setObjectName("stackedWidget")

        # fetched_data is a list of items fetched from somewhere
        for i, item in enumerate(self.listArtikel):
            new_widget = QtWidgets.QWidget()
            new_widget.setObjectName(f"page_{i+1}")
            self.stackedWidget.addWidget(new_widget)

        self.horizontalLayout_11.addWidget(self.stackedWidget)

        self.hboxlayout.addWidget(self.widget_img)
        self.horizontalLayout_5.addWidget(self.frame_img)
        self.frame_next = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_next.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_next.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_next.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_next.setObjectName("frame_next")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_next)
        self.horizontalLayout_7.setContentsMargins(27, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        if (len(self.listArtikel) != 0):
            # Btn next
            self.btn_next = QtWidgets.QPushButton(parent=self.frame_next)
            self.btn_next.setMinimumSize(QtCore.QSize(50, 50))
            self.btn_next.setMaximumSize(QtCore.QSize(50, 50))
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(path + "icons/right_arrow_circle.svg"),
                            QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btn_next.setIcon(icon2)
            self.btn_next.setIconSize(QtCore.QSize(26, 26))
            self.btn_next.setObjectName("btn_next")
            self.btn_next.setCursor(Qt.CursorShape.PointingHandCursor)
            self.horizontalLayout_7.addWidget(self.btn_next)
            self.btn_next.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))

        self.horizontalLayout_5.addWidget(
            self.frame_next, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_2.addWidget(self.frame_contents_1)
        self.frame_description = QtWidgets.QFrame(parent=self.main)
        self.frame_description.setFrameShape(
            QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_description.setObjectName("frame_description")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_description)
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.box_description_artikel = QtWidgets.QWidget(
            parent=self.frame_description)
        self.box_description_artikel.setMaximumSize(QtCore.QSize(600, 205))
        self.box_description_artikel.setObjectName("box_description_artikel")

        if (len(self.listArtikel) == 0):
            self.box_description_artikel.setMaximumSize(QtCore.QSize(0, 0))

        # Deskripsi Artikel
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.box_description_artikel)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.text_title_artikel = QtWidgets.QTextEdit(
            parent=self.box_description_artikel)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.text_title_artikel.sizePolicy().hasHeightForWidth())
        self.text_title_artikel.setSizePolicy(sizePolicy)
        self.text_title_artikel.setMaximumSize(QtCore.QSize(16777215, 45))

        self.text_title_artikel.setReadOnly(True)
        self.text_title_artikel.setObjectName("text_title_artikel")
        self.verticalLayout_4.addWidget(self.text_title_artikel)
        self.text_description_artikel = QtWidgets.QTextEdit(
            parent=self.box_description_artikel)
        self.text_description_artikel.setReadOnly(True)
        self.text_description_artikel.setObjectName("text_description_artikel")

        self.verticalLayout_4.addWidget(self.text_description_artikel)
        self.horizontalLayout_8.addWidget(self.box_description_artikel)
        self.verticalLayout_2.addWidget(self.frame_description)
        self.verticalLayout.addWidget(self.main)
        self.setCentralWidget(self.centralwidget)

        self.stackedWidget.setCurrentIndex(0)

        current_index = self.stackedWidget.currentIndex()
        if (len(self.listArtikel) != 0):
            self.change_background_img(current_index)

            self.btn_prev.clicked.connect(self.prev)
            self.btn_next.clicked.connect(self.next)

        if (len(self.listArtikel) == 0):
            self.frame_no_artikel = QtWidgets.QFrame(
                parent=self.frame_contents_1)
            self.frame_no_artikel.setFrameShape(
                QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_no_artikel.setFrameShadow(
                QtWidgets.QFrame.Shadow.Raised)
            self.frame_no_artikel.setObjectName("frame_no_artikel")

            self.vertical_layout_no_artikel = QtWidgets.QVBoxLayout(
                self.frame_no_artikel)
            self.vertical_layout_no_artikel.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_no_artikel.setSpacing(0)
            self.vertical_layout_no_artikel.setObjectName(
                "vertical_layout_no_artikel")

            self.frame_label_no_artikel = QtWidgets.QFrame(
                parent=self.frame_no_artikel)
            self.frame_label_no_artikel.setFrameShape(
                QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_label_no_artikel.setFrameShadow(
                QtWidgets.QFrame.Shadow.Raised)
            self.frame_label_no_artikel.setObjectName(
                f"frame_label_no_artikel")

            self.vertical_layout_no_artikel_2 = QtWidgets.QVBoxLayout(
                self.frame_label_no_artikel)
            self.vertical_layout_no_artikel_2.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_no_artikel_2.setSpacing(0)
            self.vertical_layout_no_artikel_2.setObjectName(
                f"vertical_layout_no_artikel_2")

            self.icon_no_artikel = QtWidgets.QLabel(
                parent=self.frame_label_no_artikel)
            self.icon_no_artikel.setFixedSize(100, 100)
            self.icon_no_artikel.setPixmap(
                QtGui.QPixmap(path + "icons/search_off.svg"))
            self.icon_no_artikel.setScaledContents(True)
            self.icon_no_artikel.setObjectName("icon_no_artikel")

            self.label_no_artikel = QtWidgets.QLabel(
                parent=self.frame_label_no_artikel)
            self.label_no_artikel.setStyleSheet('''
                                            #label_no_artikel {
                                                color: #3C6255;
                                                font-size: 24px;
                                                font-weight: 600;
                                            }
                                            ''')
            self.label_no_artikel.setObjectName("label_no_artikel")
            self.label_no_artikel.setText("No Artikel Found")

            self.vertical_layout_no_artikel.addWidget(
                self.icon_no_artikel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.vertical_layout_no_artikel.addWidget(
                self.label_no_artikel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.vertical_layout_x.addWidget(self.frame_no_artikel)

        self.btn_back.clicked.connect(self.on_btn_back_clicked)
        self.label_title_artikel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        self.widget_img.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        self.box_description_artikel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))

    def setArtikel(self):
        response = requests.get('http://127.0.0.1:3000/artikel/')

        if response.status_code == 200:
            self.listArtikel = json.loads(response.text)
        else:
            self.listArtikel = []
            print("No Artikel Found")

    def on_btn_back_clicked(self):
        self.channel.emit("main")

    def prev(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index == 0:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.count() - 1)
        else:
            self.stackedWidget.setCurrentIndex(current_index - 1)

        index = self.stackedWidget.currentIndex()
        self.change_background_img(index)

    def next(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index == self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(current_index + 1)

        index = self.stackedWidget.currentIndex()
        self.change_background_img(index)

    def change_background_img(self, index):
        self.text_title_artikel.setText(self.listArtikel[index]["judul"])
        self.text_description_artikel.setText(
            self.listArtikel[index]["isi_artikel"])
        image = self.listArtikel[index]["gambar"]

        self.widget_img.setStyleSheet(
            f"#widget_img {{border-image: url({image}) 0 0 0 0 stretch stretch; background-attachment: fixed; border-radius: 40px;}}")

        self.text_title_artikel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_description_artikel.setAlignment(
            Qt.AlignmentFlag.AlignJustify)
