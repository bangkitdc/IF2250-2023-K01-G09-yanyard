from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json, datetime

class DetailTanamanWindow(QMainWindow):
    channel = pyqtSignal(str, int, int)

    def __init__(self, idTanaman=None):
        super().__init__()
        self.idTanaman = idTanaman
        self.setUpDetailTanamanWindow()

    def setUpDetailTanamanWindow(self):
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

        if (self.idTanaman != None):
            self.setDetailTanaman(self.idTanaman)
            self.initializeWidgets(path)
        
    def initializeWidgets(self, path):
        self.setStyleSheet('''
                           *{
                                border: none;
                                padding: 0;
                                margin: 0;
                                font-family: Poppins;
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
                                        background-color: transparent;
                                    }

                                    #btn_back:hover {
                                        color: #DEDBC0;
                                        background-color: transparent;
                                    }
                                    ''')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path + "icons/left_arrow.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_temp_2)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame = QtWidgets.QFrame(parent=self.frame_temp_2)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btn_edit = QtWidgets.QPushButton(parent=self.frame)
        self.btn_edit.setStyleSheet('''
                                    #btn_edit {
                                        border-radius: 17px;
                                        height: 34px;
                                        width: 34px;
                                        margin: 2px;
                                        background-color: transparent;
                                    }
                                    
                                    #btn_edit:hover {
                                        background-color: #61876E;
                                    }
                                    ''')
        icon_edit = QtGui.QIcon()
        icon_edit.addPixmap(QtGui.QPixmap(path + "/icons/mode_edit.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_edit.setIcon(icon_edit)
        self.btn_edit.setIconSize(QtCore.QSize(24, 24))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_edit.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.horizontalLayout_15.addWidget(self.btn_edit)
        self.horizontalLayout_14.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_temp_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btn_delete = QtWidgets.QPushButton(parent=self.frame_2)
        self.btn_delete.setStyleSheet('''
                                        #btn_delete {
                                            border-radius: 17px;
                                            height: 34px;
                                            width: 34px;
                                            margin: 2px;
                                            background-color: transparent;
                                        }
                                      
                                        #btn_delete:hover {
                                            background-color: #61876E;
                                        }
                                      ''')
        self.btn_delete.setText("")
        icon_delete = QtGui.QIcon()
        icon_delete.addPixmap(QtGui.QPixmap(path + "icons/delete.svg"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_delete.setIcon(icon_delete)
        self.btn_delete.setIconSize(QtCore.QSize(24, 24))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.horizontalLayout_16.addWidget(self.btn_delete)
        self.horizontalLayout_14.addWidget(self.frame_2)
        
        self.horizontalLayout.addWidget(self.frame_temp_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addWidget(self.header)
        
        # Scroll area
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
                                            background-color: transparent;
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -243, 940, 801))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Main
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
        self.verticalLayout_3.setContentsMargins(38, 0, 18, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_tanaman = QtWidgets.QFrame(parent=self.main)
        self.frame_tanaman.setMinimumSize(QtCore.QSize(0, 380))
        self.frame_tanaman.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tanaman.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tanaman.setObjectName("frame_tanaman")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_tanaman)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_img = QtWidgets.QFrame(parent=self.frame_tanaman)
        self.frame_img.setMaximumSize(QtCore.QSize(16777215, 220))
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_img.setObjectName("frame_img")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_img)
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        # Image Tanaman
        self.widget_img = QtWidgets.QWidget(parent=self.frame_img)
        self.widget_img.setMinimumSize(QtCore.QSize(160, 200))
        self.widget_img.setMaximumSize(QtCore.QSize(160, 200))
        self.widget_img.setObjectName("widget_img")
        
        image = self.detailTanaman[0]["gambar"]
        
        if image == None or not os.path.isfile(image):
            self.widget_img.setStyleSheet(
                "#widget_img {border-image: url(assets/images/tanaman/no_photo.png) 0 0 0 0 stretch stretch; background-attachment: fixed; border-radius:40px;}")
        else:
            self.widget_img.setStyleSheet(
                    f"#widget_img {{border-image: url({image}) 0 0 0 0 stretch stretch; background-attachment: fixed; border-radius:40px;}}")
       
        self.widget_img.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_img)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6.addWidget(self.widget_img)
        self.verticalLayout_4.addWidget(self.frame_img, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_name = QtWidgets.QFrame(parent=self.frame_tanaman)
        self.frame_name.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_name.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_name.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_name.setObjectName("frame_name")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_name)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        # Name Tanaman
        self.label_name = QtWidgets.QLabel(parent=self.frame_name)
        self.label_name.setStyleSheet('''
                                        #label_name {
                                            color: #3C6255;
                                            font-size: 28px;
                                            font-weight: 800;
                                            background-color: transparent;
                                        }
                                        ''')
        self.label_name.setObjectName("label_name")
        self.label_name.setText(self.detailTanaman[0]["nama_tanaman"])
        
        self.horizontalLayout_5.addWidget(self.label_name, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_name)
        self.frame_text = QtWidgets.QFrame(parent=self.frame_tanaman)
        self.frame_text.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_text.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_text.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_text.setObjectName("frame_text")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_text)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        # Description Tanaman
        self.text_desc_tanaman = QtWidgets.QTextEdit(parent=self.frame_text)
        self.text_desc_tanaman.setStyleSheet('''
                                            #text_desc_tanaman {
                                                color: #3C6255;
                                                font-size: 14px;
                                                font-weight: 500;
                                                background-color: transparent;
                                            }
                                            ''')
        self.text_desc_tanaman.setReadOnly(True)
        self.text_desc_tanaman.setObjectName("text_desc_tanaman")
        self.text_desc_tanaman.setText(self.detailTanaman[0]["deskripsi_tanaman"])
        self.text_desc_tanaman.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.horizontalLayout_6.addWidget(self.text_desc_tanaman)
        self.verticalLayout_4.addWidget(self.frame_text)
        self.verticalLayout_3.addWidget(self.frame_tanaman)
        
        # TO DO LIST
        self.frame_tdl = QtWidgets.QFrame(parent=self.main)
        self.frame_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl.setObjectName("frame_tdl")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_tdl)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        # Head TDL
        self.frame_head_tdl = QtWidgets.QFrame(parent=self.frame_tdl)
        self.frame_head_tdl.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_head_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_tdl.setObjectName("frame_head_tdl")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_head_tdl)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_head_tdl_1 = QtWidgets.QFrame(parent=self.frame_head_tdl)
        self.frame_head_tdl_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_tdl_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_tdl_1.setObjectName("frame_head_tdl_1")
        self.icon_tdl = QtWidgets.QLabel(parent=self.frame_head_tdl_1)
        self.icon_tdl.setGeometry(QtCore.QRect(0, 15, 30, 30))
        self.icon_tdl.setPixmap(QtGui.QPixmap(path + "icons/format_list_bulleted.svg"))
        self.icon_tdl.setScaledContents(True)
        self.icon_tdl.setObjectName("icon_tdl")
        self.label_tdl = QtWidgets.QLabel(parent=self.frame_head_tdl_1)
        self.label_tdl.setGeometry(QtCore.QRect(40, 15, 120, 30))
        self.label_tdl.setStyleSheet('''
                                    #label_tdl {
                                        color: #3C6255;
                                        font-size: 24px;
                                        font-weight: 600;
                                        background-color: transparent;
                                    }
                                    ''')
        self.label_tdl.setObjectName("label_tdl")
        self.label_tdl.setText("To Do List")
        
        self.horizontalLayout_4.addWidget(self.frame_head_tdl_1)
        self.frame_head_tdl_2 = QtWidgets.QFrame(parent=self.frame_head_tdl)
        self.frame_head_tdl_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_tdl_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_tdl_2.setObjectName("frame_head_tdl_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_head_tdl_2)
        self.verticalLayout_8.setContentsMargins(-1, -1, 4, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_add_tdl = QtWidgets.QPushButton(parent=self.frame_head_tdl_2)
        self.btn_add_tdl.setMinimumSize(QtCore.QSize(170, 0))
        self.btn_add_tdl.setStyleSheet('''
                                        #btn_add_tdl{
                                            color: #F7F4D9;
                                            background-color: #61876E;
                                            padding: 15px;
                                            border-radius: 20px;
                                            font-size: 14px;
                                            font-weight: 600;
                                        }
                                        
                                        #btn_add_tdl:hover {
                                            background-color: #486E55;
                                        }
                                        ''')
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path + "icons/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_add_tdl.setIcon(icon1)
        self.btn_add_tdl.setIconSize(QtCore.QSize(20, 20))
        self.btn_add_tdl.setObjectName("btn_add_tdl")
        self.btn_add_tdl.setText("ADD TO DO LIST")
        self.btn_add_tdl.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_add_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.verticalLayout_8.addWidget(self.btn_add_tdl, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_4.addWidget(self.frame_head_tdl_2)
        self.verticalLayout_7.addWidget(self.frame_head_tdl)
        
        # List TDL
        self.frame_list_tdl = QtWidgets.QFrame(parent=self.frame_tdl)
        self.frame_list_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list_tdl.setObjectName("frame_list_tdl")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_list_tdl)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        
        # Dynamic TDL
        if (len(self.listTDL) == 0):
            self.frame_no_tdl = QtWidgets.QFrame(parent=self.frame_list_tdl)
            self.frame_no_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_no_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_no_tdl.setObjectName("frame_no_tdl")
            
            self.vertical_layout_no_tdl = QtWidgets.QVBoxLayout(self.frame_no_tdl)
            self.vertical_layout_no_tdl.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_no_tdl.setSpacing(0)
            self.vertical_layout_no_tdl.setObjectName("vertical_layout_no_tdl")
            
            self.frame_label_no_tdl = QtWidgets.QFrame(parent=self.frame_no_tdl)
            self.frame_label_no_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_label_no_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_label_no_tdl.setObjectName(f"frame_label_no_tdl")
            
            self.vertical_layout_no_tdl_2 = QtWidgets.QVBoxLayout(self.frame_label_no_tdl)
            self.vertical_layout_no_tdl_2.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_no_tdl_2.setSpacing(0)
            self.vertical_layout_no_tdl_2.setObjectName(f"vertical_layout_no_tdl_2")
            
            self.icon_no_tdl = QtWidgets.QLabel(parent=self.frame_label_no_tdl)
            self.icon_no_tdl.setFixedSize(100, 100)
            self.icon_no_tdl.setPixmap(QtGui.QPixmap(path + "icons/search_off.svg"))
            self.icon_no_tdl.setScaledContents(True)
            self.icon_no_tdl.setObjectName("icon_no_tdl")
            
            self.label_no_tdl = QtWidgets.QLabel(parent=self.frame_label_no_tdl)
            self.label_no_tdl.setStyleSheet('''
                                            #label_no_tdl {
                                                color: #3C6255;
                                                font-size: 24px;
                                                font-weight: 600;
                                                background-color: transparent;
                                            }
                                            ''')
            self.label_no_tdl.setObjectName("label_no_tdl")
            self.label_no_tdl.setText("No To Do List Found")
            
            self.vertical_layout_no_tdl.addWidget(self.icon_no_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.vertical_layout_no_tdl.addWidget(self.label_no_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.verticalLayout_10.addWidget(self.frame_no_tdl)
            
        for i, item in enumerate(self.listTDL):
            # Frame
            self.frame_tdl_temp = QtWidgets.QFrame(parent=self.frame_list_tdl)
            self.frame_tdl_temp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_tdl_temp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_tdl_temp.setObjectName(f"frame_tdl_temp_{i}")
            
            # Layout for frame
            self.horizontal_layout_temp = QtWidgets.QHBoxLayout(self.frame_tdl_temp)
            self.horizontal_layout_temp.setContentsMargins(0, 9, 4, 9)
            self.horizontal_layout_temp.setObjectName(f"horizontal_layout_temp_{i}")
            
            # Time frame
            self.frame_time_tdl = QtWidgets.QFrame(parent=self.frame_tdl_temp)
            self.frame_time_tdl.setMaximumSize(QtCore.QSize(160, 16777215))
            self.frame_time_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_time_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_time_tdl.setObjectName(f"frame_time_tdl_{i}")
            self.frame_time_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
            
            # Vert layout
            self.vertical_layout_time = QtWidgets.QVBoxLayout(self.frame_time_tdl)
            self.vertical_layout_time.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_time.setSpacing(0)
            self.vertical_layout_time.setObjectName(f"vertical_layout_time_{i}")
            
            # Label time
            self.label_time_tdl = QtWidgets.QLabel(parent=self.frame_time_tdl)
            self.label_time_tdl.setMinimumSize(QtCore.QSize(140, 40))
            self.label_time_tdl.setStyleSheet(f'''
                                            #label_time_tdl_{i} {{
                                                color: #F7F4D9;
                                                background-color: #61876E;
                                                border-radius: 16px;
                                                font-size: 14px;
                                                font-weight: 500;
                                            }}
                                            ''')
            self.label_time_tdl.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
            str_time = self.listTDL[i]["waktu"]
            date_time = datetime.datetime.strptime(str_time, "%a, %d %b %Y %H:%M:%S %Z")
            
            self.label_time_tdl.setText(date_time.strftime('%H:%M') + " │ " + date_time.strftime('%d %b'))
            self.label_time_tdl.setObjectName(f"label_time_tdl_{i}")
        
            self.vertical_layout_time.addWidget(self.label_time_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
    
            # Add time frame to horizontal layout
            self.horizontal_layout_temp.addWidget(self.frame_time_tdl)
            
            # Desc frame
            self.frame_desc = QtWidgets.QFrame(parent=self.frame_tdl_temp)
            self.frame_desc.setMinimumSize(QtCore.QSize(16777215, 40))
            self.frame_desc.setStyleSheet(f'''
                                     #frame_desc_{i} {{
                                        color: #F7F4D9;
                                        background-color: #61876E;
                                        padding: 0px 20px;
                                        border-radius: 16px;
                                    }}
                                    ''')
            self.frame_desc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_desc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_desc.setObjectName(f"frame_desc_{i}")
            self.frame_desc.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
            
            # Horizontal layout
            self.horizontal_layout_desc = QtWidgets.QHBoxLayout(self.frame_desc)
            self.horizontal_layout_desc.setContentsMargins(0, 9, 0, 9)
            self.horizontal_layout_desc.setObjectName(f"horizontal_layout_desc_{i}")
            
            # Label
            self.label_desc_tdl = QtWidgets.QLabel(parent=self.frame_desc)
            self.label_desc_tdl.setStyleSheet(f'''
                                                #label_desc_tdl_{i} {{
                                                    color: #F7F4D9;
                                                    font-size: 14px;
                                                    font-weight: 500;
                                                    background-color: transparent;
                                                }}
                                                ''')
            self.label_desc_tdl.setText(self.listTDL[i]["deskripsi_tdl"])
            self.label_desc_tdl.setObjectName(f"label_desc_tdl_{i}")
            self.horizontal_layout_desc.addWidget(self.label_desc_tdl, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
            
            self.btn_more_1 = QtWidgets.QPushButton(parent=self.frame_desc)
            self.btn_more_1.setStyleSheet("")
            self.btn_more_1.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(path + "icons/more_vert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btn_more_1.setIcon(icon2)
            self.btn_more_1.setIconSize(QtCore.QSize(20, 20))
            self.btn_more_1.setObjectName(f"btn_more_1_{i}")
            
            self.menu = QtWidgets.QMenu()
            self.edit_action = self.menu.addAction("Edit")
            self.delete_action = self.menu.addAction("Delete")

            self.menu.setStyleSheet(
                '''
                QMenu{
                    color: #F7F4D9;
                    width: 87px;
                    background-color: #3C6255;
                    }

                QMenu::item {
                    border-radius: 4px;
                    padding: 2px 25px 2px 20px;
                    border: 1px solid transparent; /* reserve space for selection border */
                }

                QMenu::item:selected{
                background-color: #61876E;
                color: #F7F4D9;
                }
                '''
            )
            str_id_tdl = self.listTDL[i]["id_tdl"]
            self.edit_action.triggered.connect(lambda checked, obj_name=f"btn_menu_tdl_{str_id_tdl}": self.handle_menu_tdl(self.edit_action, obj_name))
            self.delete_action.triggered.connect(lambda checked, obj_name=f"btn_menu_tdl_{str_id_tdl}": self.handle_menu_tdl(self.delete_action, obj_name))
            
            self.btn_more_1.setMenu(self.menu)
            self.btn_more_1.setStyleSheet("QPushButton::menu-indicator { width: 0px }")
            self.btn_more_1.setCursor(Qt.CursorShape.PointingHandCursor)
            
            self.horizontal_layout_desc.addWidget(self.btn_more_1, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.horizontal_layout_temp.addWidget(self.frame_desc)
            self.verticalLayout_10.addWidget(self.frame_tdl_temp)
                            
        # Spacer
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addWidget(self.frame_list_tdl)
        self.verticalLayout_3.addWidget(self.frame_tdl)
        
        # Jurnal
        self.frame_jurnal = QtWidgets.QFrame(parent=self.main)
        self.frame_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_jurnal.setObjectName("frame_jurnal")
        
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_jurnal)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 36)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_head_jurnal = QtWidgets.QFrame(parent=self.frame_jurnal)
        self.frame_head_jurnal.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_head_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_jurnal.setObjectName("frame_head_jurnal")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_head_jurnal)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_head_jurnal_1 = QtWidgets.QFrame(parent=self.frame_head_jurnal)
        self.frame_head_jurnal_1.setStyleSheet("")
        self.frame_head_jurnal_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_jurnal_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_jurnal_1.setObjectName("frame_head_jurnal_1")
        self.icon_jurnal = QtWidgets.QLabel(parent=self.frame_head_jurnal_1)
        self.icon_jurnal.setGeometry(QtCore.QRect(0, 15, 30, 30))
        self.icon_jurnal.setPixmap(QtGui.QPixmap(path + "icons/article.svg"))
        self.icon_jurnal.setScaledContents(True)
        self.icon_jurnal.setObjectName("icon_jurnal")
        self.label_jurnal = QtWidgets.QLabel(parent=self.frame_head_jurnal_1)
        self.label_jurnal.setGeometry(QtCore.QRect(40, 15, 210, 30))
        self.label_jurnal.setStyleSheet('''
                                        #label_jurnal {
                                            color: #3C6255;
                                            font-size: 24px;
                                            font-weight: 600;
                                        }
                                        ''')
        self.label_jurnal.setObjectName("label_jurnal")
        self.label_jurnal.setText("Jurnal Tanaman")
        
        self.horizontalLayout_9.addWidget(self.frame_head_jurnal_1)
        self.frame_head_jurnal_2 = QtWidgets.QFrame(parent=self.frame_head_jurnal)
        self.frame_head_jurnal_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_head_jurnal_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_head_jurnal_2.setObjectName("frame_head_jurnal_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_head_jurnal_2)
        self.horizontalLayout_10.setContentsMargins(-1, -1, 4, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_add_jurnal = QtWidgets.QPushButton(parent=self.frame_head_jurnal_2)
        self.btn_add_jurnal.setMinimumSize(QtCore.QSize(170, 0))
        self.btn_add_jurnal.setStyleSheet('''
                                        #btn_add_jurnal {
                                            color: #F7F4D9;
                                            background-color: #61876E;
                                            padding: 15px;
                                            border-radius: 20px;
                                            font-size: 14px;
                                            font-weight: 600;
                                        }
                                        
                                        #btn_add_jurnal:hover {
                                            background-color: #486E55;
                                        }
                                        ''')
        self.btn_add_jurnal.setIcon(icon1)
        self.btn_add_jurnal.setIconSize(QtCore.QSize(20, 20))
        self.btn_add_jurnal.setObjectName("btn_add_jurnal")
        self.btn_add_jurnal.setText("ADD JURNAL")
        self.btn_add_jurnal.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_add_jurnal.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.horizontalLayout_10.addWidget(self.btn_add_jurnal, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.horizontalLayout_9.addWidget(self.frame_head_jurnal_2)
        self.verticalLayout_12.addWidget(self.frame_head_jurnal)
        self.frame_list_jurnal = QtWidgets.QFrame(parent=self.frame_jurnal)
        self.frame_list_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list_jurnal.setObjectName("frame_list_jurnal")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_list_jurnal)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        
        # DYNAMIC Jurnal
        if (len(self.listJurnal) == 0):
            self.frame_no_jurnal = QtWidgets.QFrame(parent=self.frame_list_jurnal)
            self.frame_no_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_no_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_no_jurnal.setObjectName("frame_no_jurnal")
            
            self.vertical_layout_no_jurnal = QtWidgets.QVBoxLayout(self.frame_no_jurnal)
            self.vertical_layout_no_jurnal.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_no_jurnal.setSpacing(0)
            self.vertical_layout_no_jurnal.setObjectName("vertical_layout_no_jurnal")
            
            self.frame_label_no_jurnal = QtWidgets.QFrame(parent=self.frame_no_jurnal)
            self.frame_label_no_jurnal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_label_no_jurnal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_label_no_jurnal.setObjectName(f"frame_label_no_jurnal")
            
            self.vertical_layout_no_jurnal_2 = QtWidgets.QVBoxLayout(self.frame_label_no_jurnal)
            self.vertical_layout_no_jurnal_2.setContentsMargins(0, 0, 0, 0)
            self.vertical_layout_no_jurnal_2.setSpacing(0)
            self.vertical_layout_no_jurnal_2.setObjectName(f"vertical_layout_no_jurnal_2")
            
            self.icon_no_jurnal = QtWidgets.QLabel(parent=self.frame_label_no_jurnal)
            self.icon_no_jurnal.setFixedSize(100, 100)
            self.icon_no_jurnal.setPixmap(QtGui.QPixmap(path + "icons/search_off.svg"))
            self.icon_no_jurnal.setScaledContents(True)
            self.icon_no_jurnal.setObjectName("icon_no_jurnal")
            
            # Name Tanaman
            self.label_no_jurnal = QtWidgets.QLabel(parent=self.frame_label_no_jurnal)
            self.label_no_jurnal.setStyleSheet('''
                                            #label_no_jurnal {
                                                color: #3C6255;
                                                font-size: 24px;
                                                font-weight: 600;
                                            }
                                            ''')
            self.label_no_jurnal.setObjectName("label_no_jurnal")
            self.label_no_jurnal.setText("No Jurnal Found")

            self.vertical_layout_no_jurnal.addWidget(self.icon_no_jurnal, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.vertical_layout_no_jurnal.addWidget(self.label_no_jurnal, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.verticalLayout_13.addWidget(self.frame_no_jurnal)
        
        for i, item in enumerate(self.listJurnal):
            # Outer Frame
            self.frame_jurnal_outer = QtWidgets.QFrame(parent=self.frame_list_jurnal)
            self.frame_jurnal_outer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_jurnal_outer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_jurnal_outer.setObjectName(f"frame_jurnal_outer_{i}")
            
            self.vertical_layout_outer = QtWidgets.QVBoxLayout(self.frame_jurnal_outer)
            self.vertical_layout_outer.setContentsMargins(0, 0, 0, 18)
            self.vertical_layout_outer.setSpacing(0)
            self.vertical_layout_outer.setObjectName("vertical_layout_outer")
            
            # Frame
            self.frame_jurnal_temp = QtWidgets.QFrame(parent=self.frame_jurnal_outer)
            self.frame_jurnal_temp.setMaximumSize(QtCore.QSize(16777215, 160))
            self.frame_jurnal_temp.setStyleSheet(f'''
                                                #frame_jurnal_temp_{i} {{
                                                    color: #F7F4D9;
                                                    background-color: #3C6255;
                                                    border-radius: 30px;
                                                    margin: 4px;
                                                }}
                                                ''')
            self.frame_jurnal_temp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_jurnal_temp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_jurnal_temp.setObjectName(f"frame_jurnal_temp_{i}")
            self.frame_jurnal_temp.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
            
            # Layout for frame
            self.vertical_layout_jurnal = QtWidgets.QVBoxLayout(self.frame_jurnal_temp)
            self.vertical_layout_jurnal.setContentsMargins(0, 0, 0, 9)
            self.vertical_layout_jurnal.setSpacing(0)
            self.vertical_layout_jurnal.setObjectName("vertical_layout_jurnal")
            
            # Frame top
            self.frame_jurnal_top = QtWidgets.QFrame(parent=self.frame_jurnal_temp)
            self.frame_jurnal_top.setMaximumSize(QtCore.QSize(16777215, 60))
            self.frame_jurnal_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_jurnal_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_jurnal_top.setObjectName("frame_jurnal_top")
            self.horizontal_layout_jurnal = QtWidgets.QHBoxLayout(self.frame_jurnal_top)
            self.horizontal_layout_jurnal.setContentsMargins(27, 18, 9, 0)
            self.horizontal_layout_jurnal.setSpacing(0)
            self.horizontal_layout_jurnal.setObjectName("horizontal_layout_jurnal")
            
            # Frame left
            self.frame_left = QtWidgets.QFrame(parent=self.frame_jurnal_top)
            self.frame_left.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_left.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_left.setObjectName("frame_left")
            self.horizontal_layout_jurnal_2 = QtWidgets.QHBoxLayout(self.frame_left)
            self.horizontal_layout_jurnal_2.setContentsMargins(0, 0, 0, 0)
            self.horizontal_layout_jurnal_2.setSpacing(0)
            self.horizontal_layout_jurnal_2.setObjectName("horizontal_layout_jurnal_2")
            
            # Time
            self.label_time_jurnal = QtWidgets.QLabel(parent=self.frame_left)
            self.label_time_jurnal.setStyleSheet(f'''
                                                #label_time_jurnal_{i} {{
                                                    color: #F7F4D9;
                                                    font-size: 20px;
                                                    font-weight: 600;
                                                    background-color: #3C6255;
                                                }}
                                                ''')
            
            str_date = self.listJurnal[i]["tanggal_jurnal"]
            date = datetime.datetime.strptime(str_date, "%a, %d %b %Y %H:%M:%S %Z")
            self.label_time_jurnal.setObjectName(f"label_time_jurnal_{i}")
            self.label_time_jurnal.setText(date.strftime("%d %B %Y"))
    
            self.horizontal_layout_jurnal_2.addWidget(self.label_time_jurnal)
            self.horizontal_layout_jurnal.addWidget(self.frame_left)
            
            # Frame right
            self.frame_right = QtWidgets.QFrame(parent=self.frame_jurnal_top)
            self.frame_right.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_right.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_right.setObjectName("frame_right")
            self.vertical_layout_jurnal_1 = QtWidgets.QVBoxLayout(self.frame_right)
            self.vertical_layout_jurnal_1.setObjectName("vertical_layout_jurnal_1")
            
            # Btn more
            self.btn_more_2 = QtWidgets.QPushButton(parent=self.frame_right)
            self.btn_more_2.setStyleSheet("")
            self.btn_more_2.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(path + "icons/more_vert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.btn_more_2.setIcon(icon2)
            self.btn_more_2.setIconSize(QtCore.QSize(20, 20))
            self.btn_more_2.setObjectName("btn_more_2")

            self.btn_more_2.setStyleSheet("QPushButton::menu-indicator { width: 0px }")
            
            self.menu_2 = QtWidgets.QMenu()
            self.edit_action_2 = self.menu_2.addAction("Edit")
            self.delete_action_2 = self.menu_2.addAction("Delete")
            
            str_id_jurnal = self.listJurnal[i]["id_jurnal"]
            self.edit_action_2.triggered.connect(lambda checked, obj_name=f"btn_menu_jurnal_{str_id_jurnal}": self.handle_menu_jurnal(self.edit_action_2, obj_name))
            self.delete_action_2.triggered.connect(lambda checked, obj_name=f"btn_menu_jurnal_{str_id_jurnal}": self.handle_menu_jurnal(self.delete_action_2, obj_name))
            
            self.menu_2.setStyleSheet(
                '''
                QMenu{
                    background-color: #3C6255;
                    color: #F7F4D9;
                    width: 87px;
                    }

                QMenu::item {
                    border-radius: 4px;
                    padding: 2px 25px 2px 20px;
                    border: 1px solid transparent; /* reserve space for selection border */
                }

                QMenu::item:selected{
                background-color: #61876E;
                color: #F7F4D9;
                }
                '''
            )

            self.btn_more_2.setMenu(self.menu_2)
            
            self.btn_more_2.setCursor(Qt.CursorShape.PointingHandCursor)
            
            self.vertical_layout_jurnal_1.addWidget(self.btn_more_2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.horizontal_layout_jurnal.addWidget(self.frame_right)
            self.vertical_layout_jurnal.addWidget(self.frame_jurnal_top)
            
            # Frame bot
            self.frame_jurnal_bot = QtWidgets.QFrame(parent=self.frame_jurnal)
            self.frame_jurnal_bot.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_jurnal_bot.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_jurnal_bot.setObjectName("frame_jurnal_bot")
            
            self.horizontal_layout_jurnal_3 = QtWidgets.QHBoxLayout(self.frame_jurnal_bot)
            self.horizontal_layout_jurnal_3.setContentsMargins(24, 0, 27, 0)
            self.horizontal_layout_jurnal_3.setObjectName("horizontal_layout_jurnal_3")
            self.text_desc_jurnal = QtWidgets.QTextEdit(parent=self.frame_jurnal_bot)
            self.text_desc_jurnal.setStyleSheet(f'''
                                                #text_desc_jurnal_{i} {{
                                                    color: #F7F4D9;
                                                    font-size: 14px;
                                                    font-weight: 500;
                                                    background-color: #3C6255;
                                                }}
                                                ''')
            self.text_desc_jurnal.setObjectName(f"text_desc_jurnal_{i}")
            self.text_desc_jurnal.setText(self.listJurnal[i]["deskripsi_jurnal"])
            self.text_desc_jurnal.setAlignment(Qt.AlignmentFlag.AlignJustify)
            
            self.horizontal_layout_jurnal_3.addWidget(self.text_desc_jurnal)
            self.vertical_layout_jurnal.addWidget(self.frame_jurnal_bot)
            
            self.vertical_layout_outer.addWidget(self.frame_jurnal_temp)
            
            self.verticalLayout_13.addWidget(self.frame_jurnal_outer)
        
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addWidget(self.frame_list_jurnal)
        self.verticalLayout_3.addWidget(self.frame_jurnal)
        self.verticalLayout_2.addWidget(self.main)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.centralwidget)
        
        self.btn_back.clicked.connect(self.on_btn_back_clicked)
        self.btn_edit.clicked.connect(self.edit_tanaman)
        self.btn_delete.clicked.connect(self.delete_tanaman)
        
        self.btn_add_tdl.clicked.connect(self.add_tdl)
        self.btn_add_jurnal.clicked.connect(self.add_jurnal)
    
    def setDetailTanaman(self, idTanaman):
        responseDetail = requests.get(f'http://127.0.0.1:3000/tanaman/{idTanaman}')
        responseTDL = requests.get(f'http://127.0.0.1:3000/todolist/byidtanaman/{idTanaman}')
        responseJurnal = requests.get(f'http://127.0.0.1:3000/jurnal/byidtanaman/{idTanaman}')
        
        if responseDetail.status_code == 200:
            self.detailTanaman = json.loads(responseDetail.text)
        else:
            self.detailTanaman = []
            print("No Detail Tanaman Found")

        if responseTDL.status_code == 200:
            self.listTDL = json.loads(responseTDL.text)
        else:
            self.listTDL = []
            print("No To Do List Found")
        
        if responseJurnal.status_code == 200:
            self.listJurnal = json.loads(responseJurnal.text)
        else:
            self.listJurnal = []
            print("No Jurnal Found")
    
    def handle_menu_tdl(self, action, obj_name):
        idTDL = int(obj_name.split("_")[-1])
        if (action == self.edit_action):
            self.edit_tdl(idTDL)
        elif (action == self.delete_action):
            self.delete_tdl(idTDL)
            
    def handle_menu_jurnal(self, action, obj_name):
        idJurnal = int(obj_name.split("_")[-1])
        if (action == self.edit_action_2):
            self.edit_jurnal(idJurnal)
        elif (action == self.delete_action_2):
            self.delete_jurnal(idJurnal)
    
    def delete_tdl(self, idTDL):
        confirm = QMessageBox.critical(self, "Delete Todolist Item", "Are you sure you want to delete this to do list?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            response = requests.delete(f'http://127.0.0.1:3000/todolist/deletetodolist/{idTDL}')
            if response.status_code == 204:
                print("Todolist item deleted successfully.")
                self.setUpDetailTanamanWindow()
            else:
                print(f"Failed to delete Todolist item with id {idTDL}. Status code: {response.status_code}")
    
    def delete_jurnal(self, idJurnal):
        confirm = QMessageBox.critical(self, "Delete Todolist Item", "Are you sure you want to delete this jurnal?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            response = requests.delete(f'http://127.0.0.1:3000/jurnal/deletejurnal/{idJurnal}')
            if response.status_code == 204:
                print("Jurnal item deleted successfully.")
                self.setUpDetailTanamanWindow()
            else:
                print(f"Failed to delete Jurnal item with id {idJurnal}. Status code: {response.status_code}")
    
    def delete_tanaman(self):
        confirm = QMessageBox.critical(self, "Delete Tanaman", "Are you sure you want to delete this tanaman?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            response = requests.delete(f'http://127.0.0.1:3000/tanaman/deletetanaman/{self.idTanaman}')
            if response.status_code == 204:
                print("Tanaman deleted successfully.")
                self.channel.emit("data tanaman", None, None)
            else:
                print(f"Failed to delete Tanaman with id {self.idTanaman}. Status code: {response.status_code}")
    
    def edit_tanaman(self):
        self.channel.emit("form tanaman", self.idTanaman, None)
    
    # TDL
    def add_tdl(self):
        self.channel.emit("form tdl add", self.idTanaman, None)
    
    def edit_tdl(self, idTDL):
        self.channel.emit("form tdl edit", None, idTDL)
        
    # Jurnal
    def add_jurnal(self):
        self.channel.emit("form jurnal add", self.idTanaman, None)
        
    def edit_jurnal(self, idJurnal):
        self.channel.emit("form jurnal edit", None, idJurnal)
    
    def on_btn_back_clicked(self):
        self.channel.emit("data tanaman", None, None)