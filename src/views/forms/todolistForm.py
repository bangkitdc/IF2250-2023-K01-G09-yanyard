from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json, datetime

class TodolistForm(QMainWindow):
    channel = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setUpTodolistForm()
        self.idTDL = None
        self.fromMenu = False

    def setFromMenu(self):
        self.fromMenu = True

    def setFromDetail(self):
        self.fromMenu = False
        
    def setUpFieldsAdd(self, idTanaman):
        self.idTanaman = idTanaman
        
    def setUpFieldsEdit(self, idTDL):
        responseTDL = requests.get(f'http://127.0.0.1:3000/todolist/byidtodolist/{idTDL}')
        if responseTDL.status_code == 200:
            self.todolist = json.loads(responseTDL.text)
            
            self.idTDL = idTDL
            self.idTanaman = self.todolist[0]["id_tanaman"]
            
            mysql_date_str = self.todolist[0]["waktu"]
            datetime_obj = datetime.datetime.strptime(mysql_date_str, "%a, %d %b %Y %H:%M:%S %Z")
            
            self.date_time_edit.setDateTime(datetime_obj)
            self.deskripsi_tdl.setPlainText(self.todolist[0]["deskripsi_tdl"])
        else:
            self.todolist = []
            print("No To Do List Found")
    
    def setUpTodolistForm(self):
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
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(0, 60))
        self.header.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet('''
                                  #header {
                                      background-color: #3C6255;
                                  }
                                  ''')
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
        icon.addPixmap(QtGui.QPixmap(path + "icons/left_arrow.svg"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.btn_back.setText(" Kembali")
        self.btn_back.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_back.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
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
        self.logo.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.frame_temp_2 = QtWidgets.QFrame(parent=self.header)
        self.frame_temp_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp_2.setObjectName("frame_temp_2")
        self.horizontalLayout.addWidget(self.frame_temp_2)
        self.verticalLayout.addWidget(self.header)
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setStyleSheet('''
                                #body {
                                    background-color: #F7F4D9;
                                }
                                ''')
        self.main.setObjectName("body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 18, -1, -1)
        self.label_title_form = QtWidgets.QLabel(parent=self.frame_title)
        self.label_title_form.setMinimumSize(QtCore.QSize(238, 68))
        self.label_title_form.setStyleSheet('''
                                            #label_title_form {
                                                color: #F7F4D9;
                                                background-color: #3C6255;
                                                padding: 15px 0px;
                                                border-radius: 25px;
                                                font-size: 24px;
                                                font-weight: 600;
                                            }
                                            ''')
        self.label_title_form.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title_form.setObjectName("label_title_form")
        self.label_title_form.setText("Form ToDoList")
        self.label_title_form.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_4.addWidget(self.label_title_form, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_contents_1 = QtWidgets.QFrame(parent=self.main)
        self.frame_contents_1.setMaximumSize(QtCore.QSize(16777215, 210))
        self.frame_contents_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contents_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contents_1.setObjectName("frame_contents_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_contents_1)
        self.verticalLayout_3.setContentsMargins(-1, 45, -1, 18)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.date_time_edit = QtWidgets.QDateTimeEdit(parent=self.frame)
        self.date_time_edit.setMinimumSize(QtCore.QSize(200, 35))
        self.date_time_edit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.date_time_edit.setStyleSheet('''
                                          QDateTimeEdit {
                                              padding: 0px 0px 0px 12px;
                                              border-radius: 17px;
                                              background-color: #61876E;
                                              color: #F7F3D7;
                                              font-size: 14px;
                                              font-weight: 600;
                                              border: solid;
                                          }
                                          
                                          QDateTimeEdit::drop-down{
                                              image: url(assets/icons/event_note.svg);
                                              width: 20px;
                                              padding: 0px 12px 0px 8px;
                                              border-top-right-radius: 17px;
                                              border-bottom-right-radius: 17px;
                                          }
                                          
                                          QDateTimeEdit::drop-down:hover{
                                              background-color: #3C6255;
                                          }
                                          
                                          QCalendarWidget QToolButton {
                                              color: black;
                                          }
                                          
                                          QCalendarWidget QToolButton:hover {
                                              background-color: #61876E;
                                          }
                                          
                                          QCalendarWidget QAbstractItemView:enabled {
                                              selection-background-color: #61876E;
                                              selection-color: #fff; 
                                          }
                                          ''')
        self.date_time_edit.setCurrentSection(
            QtWidgets.QDateTimeEdit.Section.DaySection)
        self.date_time_edit.setObjectName("date_time_edit")
        self.date_time_edit.setCalendarPopup(True)
        self.date_time_edit.setDisplayFormat("dd-MM-yyyy h:mm AP")
        self.date_time_edit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date_time_edit.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
        self.date_time_edit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.verticalLayout_4.addWidget(self.date_time_edit)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_2.setMinimumSize(QtCore.QSize(330, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(330, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.deskripsi_tdl = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        self.deskripsi_tdl.setMinimumSize(QtCore.QSize(0, 45))
        self.deskripsi_tdl.setMaximumSize(QtCore.QSize(330, 45))
        self.deskripsi_tdl.setStyleSheet('''
                                         #deskripsi_tdl {
                                             padding: 7px 12px;
                                             border-radius: 20px;
                                             background: #61876E;
                                             color: #F7F3D7;
                                             font-size: 14px;
                                             font-weight: 600;
                                         }
                                         ''')
        self.deskripsi_tdl.setMaximumBlockCount(1)
        self.deskripsi_tdl.setObjectName("deskripsi_tdl")
        self.deskripsi_tdl.setPlaceholderText("Tuliskan ToDoList-mu yah . . .")
        self.deskripsi_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.verticalLayout_5.addWidget(self.deskripsi_tdl)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame_contents_1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_description = QtWidgets.QFrame(parent=self.main)
        self.frame_description.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_description.setObjectName("frame_description")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_description)
        self.horizontalLayout_5.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_submit = QtWidgets.QPushButton(parent=self.frame_description)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_submit.sizePolicy().hasHeightForWidth())
        self.btn_submit.setSizePolicy(sizePolicy)
        self.btn_submit.setMinimumSize(QtCore.QSize(130, 40))
        self.btn_submit.setStyleSheet('''
                                      #btn_submit {
                                          border-radius: 20px;
                                          background: #3C6255;
                                          color: #F7F3D7;
                                          font-size: 16px;
                                          font-weight: 600;
                                      }
                                      
                                      #btn_submit:hover {
                                          background-color: #23493C;
                                      }
                                      ''')
        self.btn_submit.setDefault(False)
        self.btn_submit.setFlat(False)
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.setText("Submit")
        self.btn_submit.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_submit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.horizontalLayout_5.addWidget(self.btn_submit, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_description)
        self.verticalLayout.addWidget(self.main)
        self.setCentralWidget(self.centralwidget)
        
        self.btn_back.clicked.connect(self.on_btn_back_clicked)
        self.btn_submit.clicked.connect(self.validate_input)
        
    def clear_data(self):        
        self.date_time_edit.setMinimumDateTime(QtCore.QDateTime.currentDateTime())
        self.deskripsi_tdl.clear()

    def on_btn_back_clicked(self):
        self.clear_data()
        if (self.fromMenu):
            self.channel.emit("tdl", None)
        else:
            self.channel.emit("detail", self.idTanaman)
        
    def is_todolist_null(self):
        return self.deskripsi_tdl.toPlainText().strip() == ""

    def is_todolist_too_long(self):
        return len(self.deskripsi_tdl.toPlainText().strip()) > 255

    def validate_input(self):
        if self.is_todolist_null():
            QMessageBox.warning(self, "Error", "Deskripsi To Do List Kosong")
        elif self.is_todolist_too_long():
            QMessageBox.warning(self, "Error", "Deskripsi To Do List Terlalu Panjang")
        else:
            if (self.idTDL == None): # Insert
                # masukin ke database dan balik ke data tanaman page
                
                date_time = self.date_time_edit.dateTime()
                date_time_str = date_time.toString()
                date_obj = datetime.datetime.strptime(date_time_str, "%a %b %d %H:%M:%S %Y")
                mysql_date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                
                data = {
                    "id_tanaman": self.idTanaman,
                    "waktu": mysql_date_str,
                    "deskripsi_tdl": self.deskripsi_tdl.toPlainText().strip()
                }
                response = requests.post(f'http://127.0.0.1:3000/todolist/addtodolist', data=data)
                if response.status_code == 201:
                    print("To Do List added successfully.")
                    self.nextPage(self.idTanaman)
                else:
                    print(f"Failed to add To Do List. Status code: {response.status_code}")
            else: # Edit
                date_time = self.date_time_edit.dateTime()
                date_time_str = date_time.toString()
                date_obj = datetime.datetime.strptime(date_time_str, "%a %b %d %H:%M:%S %Y")
                mysql_date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
                
                data = {
                    "waktu": mysql_date_str,
                    "deskripsi_tdl": self.deskripsi_tdl.toPlainText().strip()
                }
                response = requests.put(f'http://127.0.0.1:3000/todolist/edittodolist/{self.idTDL}', data=data)
                if response.status_code == 200:
                    print("To Do List updated successfully.")
                    self.nextPage(self.jurnal[0]["id_tanaman"])
                else:
                    print(f"Failed to update To Do List. Status code: {response.status_code}")

    def nextPage(self, ids):
        self.clear_data()
        if (self.fromMenu):
            self.channel.emit("tdl", None)
        else:
            self.channel.emit("detail", ids)