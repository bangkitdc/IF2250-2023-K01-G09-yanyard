from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json, datetime


class TodolistWindow(QMainWindow):
    channel = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setUpTodolistWindow()

    def setUpTodolistWindow(self):
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

        self.setTodolist()
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
                                    }
                                    
                                    #btn_back:hover {
                                        color: #DEDBC0;
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
        self.horizontalLayout.addWidget(self.frame_temp_2)
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
                                            background: transparent;
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
        self.verticalLayout_3.setContentsMargins(36, -1, 36, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_title = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 36)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_title_tdl = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_tdl.setMaximumSize(QtCore.QSize(238, 16777215))
        self.label_title_tdl.setStyleSheet('''
                                            #label_title_tdl {
                                                color: #F7F4D9;
                                                background-color: #3C6255;
                                                padding: 15px 50px;
                                                border-radius: 25px;
                                                font-size: 28px;
                                                font-weight: 600;
                                            }
                                            ''')
        self.label_title_tdl.setObjectName("label_title_tdl")
        self.label_title_tdl.setText("To Do List")
        self.label_title_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_5.addWidget(self.label_title_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_title)
        self.frame_tdl = QtWidgets.QFrame(parent=self.main)
        self.frame_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl.setObjectName("frame_tdl")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_tdl)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        # DYNAMIC TDL
        i = 0
        for date, tdls in self.groupsTDL.items():
            self.frame_tdls = QtWidgets.QFrame(parent=self.frame_tdl)
            self.frame_tdls.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_tdls.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_tdls.setObjectName("frame_tdls")
            
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_tdls)
            self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_6.setSpacing(0)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            
            self.frame_tanggal = QtWidgets.QFrame(parent=self.frame_tdls)
            self.frame_tanggal.setMinimumSize(QtCore.QSize(0, 50))
            self.frame_tanggal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_tanggal.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_tanggal.setObjectName("frame_tanggal")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_tanggal)
            self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.icon_tdl = QtWidgets.QLabel(parent=self.frame_tanggal)
            self.icon_tdl.setMaximumSize(QtCore.QSize(30, 30))
            self.icon_tdl.setPixmap(QtGui.QPixmap(path + "icons/event_note_green.svg"))
            self.icon_tdl.setScaledContents(True)
            self.icon_tdl.setObjectName("icon_tdl")
            self.horizontalLayout_4.addWidget(self.icon_tdl)
            self.label_tdl = QtWidgets.QLabel(parent=self.frame_tanggal)
            self.label_tdl.setStyleSheet(f'''
                                        #label_tdl_{i} {{
                                            color: #3C6255;
                                            font-size: 24px;
                                            font-weight: 600;
                                        }}
                                        ''')
            self.label_tdl.setObjectName(f"label_tdl_{i}")
            date = datetime.datetime.strptime(date, "%a, %d %b %Y").date()
            
            self.label_tdl.setText(date.strftime("%d %B %Y"))
            
            self.horizontalLayout_4.addWidget(self.label_tdl)
            self.verticalLayout_6.addWidget(self.frame_tanggal)
            
            self.frame_list_tdl = QtWidgets.QFrame(parent=self.frame_tdls)
            self.frame_list_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_list_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_list_tdl.setObjectName("frame_list_tdl")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_list_tdl)
            self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_7.setSpacing(0)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.verticalLayout_10 = QtWidgets.QVBoxLayout()
            self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout_10.setSpacing(0)
            self.verticalLayout_10.setObjectName("verticalLayout_10")
            
            # DYNAMIC
            count = 0
            for tdl in tdls:
                self.frame_tdl_1 = QtWidgets.QFrame(parent=self.frame_list_tdl)
                self.frame_tdl_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_tdl_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_tdl_1.setObjectName("frame_tdl_1")
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_tdl_1)
                self.horizontalLayout_7.setContentsMargins(0, 9, 10, 9)
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                self.frame_time_tdl_1 = QtWidgets.QFrame(parent=self.frame_tdl_1)
                self.frame_time_tdl_1.setMaximumSize(QtCore.QSize(120, 16777215))
                self.frame_time_tdl_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_time_tdl_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_time_tdl_1.setObjectName("frame_time_tdl_1")
                self.frame_time_tdl_1.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
                
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_time_tdl_1)
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName("verticalLayout_11")
                self.label_time_tdl = QtWidgets.QLabel(parent=self.frame_time_tdl_1)
                self.label_time_tdl.setMinimumSize(QtCore.QSize(100, 40))
                self.label_time_tdl.setStyleSheet(f'''
                                                    #label_time_tdl_{count} {{
                                                        color: #F7F4D9;
                                                        background-color: #61876E;
                                                    
                                                        border-radius: 16px;
                                                        font-size: 14px;
                                                        font-weight: 600;
                                                    }}
                                                    ''')
                self.label_time_tdl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                
                self.label_time_tdl.setObjectName(f"label_time_tdl_{count}")
                str_time = tdl["waktu"]
                date_time = datetime.datetime.strptime(str_time, "%a, %d %b %Y %H:%M:%S %Z")
                
                self.label_time_tdl.setText(date_time.strftime('%H:%M'))

                self.verticalLayout_11.addWidget(self.label_time_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
                self.horizontalLayout_7.addWidget(self.frame_time_tdl_1)
                self.frame_desc_tdl = QtWidgets.QFrame(parent=self.frame_tdl_1)
                self.frame_desc_tdl.setMinimumSize(QtCore.QSize(0, 40))
                self.frame_desc_tdl.setStyleSheet('''
                                                    #frame_desc_tdl {
                                                        color: #F7F4D9;
                                                        background-color: #61876E;
                                                        padding: 0px 20px;
                                                        border-radius: 16px;
                                                    }
                                                    ''')
                self.frame_desc_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_desc_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_desc_tdl.setObjectName("frame_desc_tdl")
                self.frame_desc_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
                
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_desc_tdl)
                self.horizontalLayout_8.setContentsMargins(0, 9, 0, 9)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.label_desc_tdl = QtWidgets.QLabel(parent=self.frame_desc_tdl)
                self.label_desc_tdl.setStyleSheet(f'''
                                                    #label_desc_tdl_{count} {{
                                                        color: #F7F4D9;
                                                        font-size: 14px;
                                                        font-weight: 600;
                                                    }}
                                                    ''')
                self.label_desc_tdl.setObjectName(f"label_desc_tdl_{count}")
                # self.label_desc_tdl.setText(tdl["deskripsi_tdl"] + "(" + tdl["nama_tanaman"] + ")")
                self.label_desc_tdl.setText(tdl["deskripsi_tdl"])
                
                self.horizontalLayout_8.addWidget(self.label_desc_tdl, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
                
                self.btn_more_1 = QtWidgets.QPushButton(parent=self.frame_desc_tdl)
                self.btn_more_1.setStyleSheet("")
                self.btn_more_1.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(path + "icons/more_vert.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btn_more_1.setIcon(icon1)
                self.btn_more_1.setIconSize(QtCore.QSize(20, 20))
                self.btn_more_1.setObjectName(f"btn_more_1_{count}")
                
                self.menu = QtWidgets.QMenu()
                self.edit_action = self.menu.addAction("Edit")
                self.delete_action = self.menu.addAction("Delete")

                self.menu.setStyleSheet(
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
                
                str_id_tdl = tdl["id_tdl"]
                self.edit_action.triggered.connect(lambda checked, obj_name=f"btn_menu_tdl_{str_id_tdl}": self.handle_menu_tdl(self.edit_action, obj_name))
                self.delete_action.triggered.connect(lambda checked, obj_name=f"btn_menu_tdl_{str_id_tdl}": self.handle_menu_tdl(self.delete_action, obj_name))
                
                self.btn_more_1.setMenu(self.menu)
                self.btn_more_1.setStyleSheet("QPushButton::menu-indicator { width: 0px }")
                self.btn_more_1.setCursor(Qt.CursorShape.PointingHandCursor)
                
                self.horizontalLayout_8.addWidget(self.btn_more_1, 0, QtCore.Qt.AlignmentFlag.AlignRight)
                
                self.horizontalLayout_7.addWidget(self.frame_desc_tdl)
                self.verticalLayout_10.addWidget(self.frame_tdl_1)
                self.verticalLayout_7.addLayout(self.verticalLayout_10)
                
                count += 1
            self.verticalLayout_6.addWidget(self.frame_list_tdl)
            self.verticalLayout_4.addWidget(self.frame_tdls)
            self.verticalLayout_5.addLayout(self.verticalLayout_4)
            self.verticalLayout_3.addWidget(self.frame_tdl)
            spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
            self.verticalLayout_10.addItem(spacerItem)
            i += 1
            
        if (len(self.listTodolist) > 3):
            self.verticalLayout_3.setContentsMargins(56, -1, 36, -1)
        
        # Spacer
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.main)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.setCentralWidget(self.centralwidget)
        
        self.btn_back.clicked.connect(self.on_btn_back_clicked)

    def setTodolist(self):
        response = requests.get('http://127.0.0.1:3000/todolist')

        if response.status_code == 200:
            self.listTodolist = json.loads(response.text)
            
            self.groupsTDL = {}
            for tdl in self.listTodolist:
                # Parse the date from the string
                date = datetime.datetime.strptime(tdl["waktu"], "%a, %d %b %Y %H:%M:%S %Z").date()
                
                # Use the date as the group key
                key = date.strftime("%a, %d %b %Y")
                
                # Add the task to the group
                if key in self.groupsTDL:
                    self.groupsTDL[key].append(tdl)
                else:
                    self.groupsTDL[key] = [tdl]
                
        else:
            self.listTodolist = []
            self.groupsTDL = {}
            print("No To Do List Found")
            
    def on_btn_back_clicked(self):
        self.channel.emit("main", None)
        
    def handle_menu_tdl(self, action, obj_name):
        idTDL = int(obj_name.split("_")[-1])
        if (action == self.edit_action):
            self.channel.emit("form tdl edit", idTDL)
        elif (action == self.delete_action):
            self.delete_tdl(idTDL)
    
    def delete_tdl(self, idTDL):
        # ask user if they want to delete the item
        confirm = QMessageBox.critical(self, "Delete Todolist Item", "Are you sure you want to delete this to do list?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            # send delete request
            response = requests.delete(f'http://127.0.0.1:3000/todolist/deletetodolist/{idTDL}')
            
            if response.status_code == 204:
                print("Todolist item deleted successfully.")
                self.setUpTodolistWindow()
            else:
                print(f"Failed to delete Todolist item with id {idTDL}. Status code: {response.status_code}")