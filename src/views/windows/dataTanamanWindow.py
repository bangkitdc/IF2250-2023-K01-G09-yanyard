from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json, datetime


class DataTanamanWindow(QMainWindow):
    channel = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setUpDataTanamanWindow()

    def setUpDataTanamanWindow(self):
        self.resize(960, 600)

        # Get the size and position of the user's screen
        primary_screen = QGuiApplication.primaryScreen()
        screen = primary_screen.availableGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Center the window on the screen
        self.move(int((screen_width - self.width()) / 2),
                  int((screen_height - self.height()) / 2))

        # Assets path
        path = str(pathlib.Path(__file__).parent.absolute()) + '/../../../assets/'

        # Fonts
        fonts_folder_path = path + 'fonts/'
        for filename in os.listdir(fonts_folder_path):
            if filename.endswith('.ttf') or filename.endswith('.otf'):
                font_path = os.path.join(fonts_folder_path, filename)
                QFontDatabase.addApplicationFont(font_path)

        self.setDataTanaman()
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
                            ''')
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(parent=self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setStyleSheet('''
                                    #header {
                                        background-color: #3C6255;
                                    }
                                    ''')
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
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
        self.btn_back.setStyleSheet('''
                                    #btn_back {
                                        color: #F7F4D9;
                                        font-size: 20px;
                                        font-weight: 600;
                                    }
                                    
                                    #btn_back:hover {
                                        color: #DEDBC0;
                                    }
                                    ''')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path + "/icons/left_arrow.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText(" Kembali")
        self.btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_back.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_3.addWidget(self.btn_back, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
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
        self.logo.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.frame_temp_2 = QtWidgets.QFrame(parent=self.header)
        self.frame_temp_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp_2.setObjectName("frame_temp_2")
        self.horizontalLayout.addWidget(self.frame_temp_2)
        self.verticalLayout.addWidget(self.header)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setStyleSheet('''
                                        #scrollArea {
                                            background-color: #F7F4D9;
                                        }
                                        
                                        QScrollBar:vertical {
                                            border: none;
                                            width: 20px;
                                            margin: 5px;
                                            border-radius: 0px;
                                         }
                                        
                                        /*  HANDLE BAR VERTICAL */
                                        QScrollBar::handle:vertical {    
                                            background-color: #3C6255;
                                            min-height: 20px;
                                            border-radius: 5px;
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setStyleSheet('''
                                #main {
                                    background-color: #F7F4D9;
                                }
                                ''')
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setContentsMargins(18, -1, 18, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_title = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_title_tdl = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_tdl.setMinimumSize(QtCore.QSize(248, 68))
        self.label_title_tdl.setStyleSheet('''
                                            #label_title_tdl {
                                                color: #F7F4D9;
                                                background-color: #3C6255;
                                                border-radius: 25px;
                                                font-size: 24px;
                                                font-weight: 600;
                                            }
                                            ''')
        self.label_title_tdl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title_tdl.setObjectName("label_title_tdl")
        self.label_title_tdl.setText("Data Tanaman")
        self.label_title_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_5.addWidget(self.label_title_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_title)
        self.frame_data_tanaman = QtWidgets.QFrame(parent=self.main)
        self.frame_data_tanaman.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_data_tanaman.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_data_tanaman.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_data_tanaman.setObjectName("frame_data_tanaman")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_data_tanaman)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.grid_layout_tanaman = QtWidgets.QGridLayout()
        self.grid_layout_tanaman.setHorizontalSpacing(18)
        self.grid_layout_tanaman.setVerticalSpacing(45)
        self.grid_layout_tanaman.setObjectName("grid_layout_tanaman")
        
        self.grid_layout_tanaman.setColumnStretch(1, 1)
        self.grid_layout_tanaman.setColumnStretch(1, 1)
        self.grid_layout_tanaman.setColumnStretch(1, 1)
        
        # DYNAMIC Tanaman
        for i in range(len(self.listTanaman)):
            self.frame_tanaman_1 = QtWidgets.QFrame(parent=self.frame_data_tanaman)
            self.frame_tanaman_1.setMinimumSize(QtCore.QSize(0, 220))
            self.frame_tanaman_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_tanaman_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_tanaman_1.setObjectName("frame_tanaman_1")
            self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_tanaman_1)
            self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_4.setSpacing(0)
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.frame_nama = QtWidgets.QFrame(parent=self.frame_tanaman_1)
            self.frame_nama.setMaximumSize(QtCore.QSize(16777215, 40))
            self.frame_nama.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_nama.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_nama.setObjectName("frame_nama")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_nama)
            self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_4.setSpacing(0)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label_name = QtWidgets.QLabel(parent=self.frame_nama)
            self.label_name.setStyleSheet('''
                                            #label_name {
                                                color: #3C6255;
                                                font-size: 20px;
                                                font-weight: 800;
                                            }
                                            ''')
            self.label_name.setObjectName("label_name")
            self.label_name.setText(self.listTanaman[i]["nama_tanaman"])
            
            self.horizontalLayout_4.addWidget(self.label_name, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            self.verticalLayout_4.addWidget(self.frame_nama)
            self.frame_img = QtWidgets.QFrame(parent=self.frame_tanaman_1)
            self.frame_img.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_img.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_img.setObjectName("frame_img")
            self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_img)
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            
            self.widget_img = QtWidgets.QPushButton(parent=self.frame_img)
            self.widget_img.setMinimumSize(QtCore.QSize(123, 150))
            
            image = self.listTanaman[i]["gambar"]
            idTanaman = self.listTanaman[i]["id_tanaman"]
            
            if image == None or not os.path.isfile(image):
                self.widget_img.setStyleSheet(
                    f"#widget_img_{idTanaman} {{border-image: url(assets/images/tanaman/no_photo.png) 0 0 0 0 stretch stretch; background-attachment: fixed; border-radius:30px;}}")
            else:
                self.widget_img.setStyleSheet(
                        f"#widget_img_{idTanaman} {{border-image: url({image}) 0 0 0 0 stretch stretch; background-attachment: fixed; border-radius:30px;}}")

            self.widget_img.setObjectName(f"widget_img_{idTanaman}")
            
            self.widget_img.clicked.connect(lambda checked, obj_name=f"widget_img_{idTanaman}": self.on_img_clicked(obj_name))
            self.widget_img.setCursor(Qt.CursorShape.PointingHandCursor)
            self.widget_img.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
            
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_img)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_7.setSpacing(0)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.verticalLayout_8.addWidget(self.widget_img, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            self.verticalLayout_4.addWidget(self.frame_img)
            self.frame_date = QtWidgets.QFrame(parent=self.frame_tanaman_1)
            self.frame_date.setMaximumSize(QtCore.QSize(16777215, 20))
            self.frame_date.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_date.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_date.setObjectName("frame_date")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_date)
            self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            self.label_date = QtWidgets.QLabel(parent=self.frame_date)
            self.label_date.setStyleSheet('''
                                            #label_date {
                                                color: #61876E;
                                                font-size: 11px;
                                                font-weight: 600;
                                            }
                                            ''')
            self.label_date.setObjectName("label_date")
            
            str_time = self.listTanaman[i]["tanggal_tanaman"]
            date_time = datetime.datetime.strptime(str_time, "%a, %d %b %Y %H:%M:%S %Z")
            
            self.label_date.setText(f"since {date_time.strftime('%B %Y')}")
            
            self.verticalLayout_6.addWidget(self.label_date, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
            self.verticalLayout_4.addWidget(self.frame_date)
            self.grid_layout_tanaman.addWidget(self.frame_tanaman_1, i // 3, i % 3, 1, 1)
            
        self.grid_layout_tanaman.setColumnStretch(0, 1)
        self.grid_layout_tanaman.setColumnStretch(1, 1)
        self.grid_layout_tanaman.setColumnStretch(2, 1)
        self.grid_layout_tanaman.setRowStretch(0, 1)
        self.verticalLayout_5.addLayout(self.grid_layout_tanaman)
        self.verticalLayout_3.addWidget(self.frame_data_tanaman)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.main)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.centralwidget)
        
        if (len(self.listTanaman) > 3):
            self.verticalLayout_3.setContentsMargins(38, -1, 18, -1)
        
        self.add_btn = QtWidgets.QPushButton(parent=self)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setMinimumSize(QtCore.QSize(160, 40))
        self.add_btn.setMaximumSize(QtCore.QSize(160, 40))

        size = self.size()
        self.add_btn.setGeometry(QtCore.QRect(size.width() - 220, size.height() - 80, 170, 42))
        self.add_btn.setStyleSheet('''
                                    #add_btn {
                                        color: #F7F4D9;
                                        background-color: #61876E;
                                        padding: 10px;
                                        border-radius: 20px;
                                        font-size: 14px;
                                        font-weight: 800;
                                    }
                                    ''')

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path + "icons/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_btn.setIcon(icon1)
        self.add_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_btn.setText("ADD TANAMAN")
        self.add_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.add_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        self.add_btn.clicked.connect(self.addTanaman)
        
        self.btn_back.clicked.connect(self.on_btn_back_clicked)
        
    def resizeEvent(self, event):
        # Update the position of the button when the window is resized
        button_pos = QtCore.QPoint(event.size().width() - 220, event.size().height() - 80)
        self.add_btn.move(button_pos)
        
    def setDataTanaman(self):
        response = requests.get('http://127.0.0.1:3000/tanaman/')

        if response.status_code == 200:
            self.listTanaman = json.loads(response.text)
        else:
            self.listTanaman = []
            print("No Tanaman Found")
    
    def on_img_clicked(self, obj_name):
        idTanaman = int(obj_name.split("_")[-1])
        self.channel.emit("detail", idTanaman)
    
    def addTanaman(self):
        self.channel.emit("form tanaman", None)
        
    def on_btn_back_clicked(self):
        self.channel.emit("main", None)