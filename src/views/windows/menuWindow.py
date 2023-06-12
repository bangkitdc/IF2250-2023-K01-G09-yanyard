from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QGuiApplication, QCursor, QFontDatabase, QIcon
from PyQt6.QtCore import Qt, pyqtSignal, QDateTime
import os, pathlib, requests, json, datetime

class MenuWindow(QMainWindow):
    channel = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setUpMenuWindow()
    
    def setUpMenuWindow(self):
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
            * {
                border: none;
                padding: 0;
                margin: 0;
                font-family: Poppins;
            }
            
            #header {
                background-color: #3C6255;
            }
            
            #main, #footer {
                background-color: #F7F4D9;
            }
            
            #btn_tanaman {
                padding: 5px 10px;
                border-radius: 28px;
                background: #3C6255;
                color: #F7F3D7;
                height: 46px;
                width: 243px;
                font-size: 20px;
                font-weight: 600;
            }
            
            #btn_tdl {
                padding: 5px 10px;
                border-radius: 28px;
                background: #3C6255;
                color: #F7F3D7;
                height: 46px;
                width: 243px;
                font-size: 20px;
                font-weight: 600;
            }
            
            #btn_artikel {
                padding: 5px 10px;
                border-radius: 28px;
                background: #3C6255;
                color: #F7F3D7;
                height: 46px;
                width: 243px;
                font-size: 20px;
                font-weight: 600;
            }
            
            #btn_tanaman:hover {
                background-color: #23493C;
            }
            
            #btn_tdl:hover {
                background-color: #23493C;
            }
            
            #btn_artikel:hover {
                background-color: #23493C;
            }
        ''')
        
        # Size Policy
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setAnimated(True)
        self.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        
        # Layouts
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setStyleSheet("")
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
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_logo = QtWidgets.QFrame(parent=self.header)
        self.frame_logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(parent=self.frame_logo)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setMaximumSize(QtCore.QSize(42, 42))
        self.logo.setPixmap(QtGui.QPixmap(path + 'logo/logo_circle.png'))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.logo.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_3.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Main
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Big Logo
        self.frame_logo_2 = QtWidgets.QFrame(parent=self.main)
        self.frame_logo_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo_2.setObjectName("frame_logo_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_logo_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logo_2 = QtWidgets.QLabel(parent=self.frame_logo_2)
        self.logo_2.setMaximumSize(QtCore.QSize(350, 190))
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap(path + 'logo/logo_big.png'))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName("logo_2")
        self.horizontalLayout_4.addWidget(self.logo_2)
        self.verticalLayout_2.addWidget(self.frame_logo_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_btn = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
        self.frame_btn.sizePolicy().hasHeightForWidth())
        self.frame_btn.setSizePolicy(sizePolicy)
        self.frame_btn.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        
        # Buttons
        self.frame_btn.setObjectName("frame_btn")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_btn)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        # Button Tanaman
        self.frame_tanaman = QtWidgets.QFrame(parent=self.frame_btn)
        self.frame_tanaman.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tanaman.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tanaman.setObjectName("frame_tanaman")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_tanaman)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_tanaman = QtWidgets.QPushButton(parent=self.frame_tanaman)
        self.btn_tanaman.setMouseTracking(True)
        self.btn_tanaman.setDefault(False)
        self.btn_tanaman.setFlat(False)
        self.btn_tanaman.setObjectName("btn_tanaman")
        self.btn_tanaman.setText("Data Tanaman")
        self.btn_tanaman.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tanaman.clicked.connect(self.on_btn_tanaman_clicked)
        self.verticalLayout_4.addWidget(self.btn_tanaman, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_tanaman)
        
        # Button TDL
        self.frame_tdl = QtWidgets.QFrame(parent=self.frame_btn)
        self.frame_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl.setObjectName("frame_tdl")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_tdl)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_tdl = QtWidgets.QPushButton(parent=self.frame_tdl)
        self.btn_tdl.setMouseTracking(True)
        self.btn_tdl.setDefault(False)
        self.btn_tdl.setFlat(False)
        self.btn_tdl.setObjectName("btn_tdl")
        self.btn_tdl.setText("To Do List")
        self.btn_tdl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tdl.clicked.connect(self.on_btn_tdl_clicked)
        self.verticalLayout_5.addWidget(self.btn_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_tdl)
        
        # Button Artikel
        self.frame_artikel = QtWidgets.QFrame(parent=self.frame_btn)
        self.frame_artikel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_artikel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_artikel.setObjectName("frame_artikel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_artikel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_artikel = QtWidgets.QPushButton(parent=self.frame_artikel)
        self.btn_artikel.setMouseTracking(True)
        self.btn_artikel.setDefault(False)
        self.btn_artikel.setFlat(False)
        self.btn_artikel.setObjectName("btn_artikel")
        self.btn_artikel.setText("Artikel")
        self.btn_artikel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_artikel.clicked.connect(self.on_btn_artikel_clicked)
        self.verticalLayout_6.addWidget(self.btn_artikel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_artikel)
        self.verticalLayout_2.addWidget(self.frame_btn)
        self.verticalLayout.addWidget(self.main)
        
        # Footer (additional space)
        self.footer = QtWidgets.QWidget(parent=self.centralwidget)
        self.footer.setMinimumSize(QtCore.QSize(0, 60))
        self.footer.setObjectName("footer")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(parent=self.footer)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7.addWidget(self.frame)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.setCentralWidget(self.centralwidget)
        
        self.btn_tanaman.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        self.btn_tdl.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        self.btn_artikel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
    
        self.notification_timer = QtCore.QTimer(self)
        self.notification_timer.timeout.connect(self.check_notifications)
        self.notification_timer.start(60000 * 5)
    
    def on_btn_tanaman_clicked(self):
        self.channel.emit("data tanaman")
        
    def on_btn_tdl_clicked(self):
        self.channel.emit("todolist")
        
    def on_btn_artikel_clicked(self):
        self.channel.emit("artikel")
        
    def check_notifications(self):
        # Get all idTDLs from your database
        responseTDLs = requests.get('http://127.0.0.1:3000/todolist')
        if responseTDLs.status_code == 200:
            todolist = json.loads(responseTDLs.text)
            deskripsi = todolist[0]["deskripsi_tdl"]
            mysql_date_str = todolist[0]["waktu"]
            deskripsi = todolist[0]["deskripsi_tdl"]
            datetime_obj = datetime.datetime.strptime(mysql_date_str, "%a, %d %b %Y %H:%M:%S %Z")
            current_time = datetime.datetime.now()
            
            time_diff = datetime_obj - current_time
            
            if time_diff <= datetime.timedelta(minutes=15):
                QMessageBox.information(self, "Notif", f"Sudah saatnya kamu {deskripsi}")
                    
