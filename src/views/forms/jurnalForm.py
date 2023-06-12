from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json, datetime

class JurnalForm(QMainWindow):
    channel = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setUpJurnalForm()
        self.idJurnal = None
        
    def setUpFieldsAdd(self, idTanaman):
        self.idTanaman = idTanaman
        
    def setUpFieldsEdit(self, idJurnal):
        responseJurnal = requests.get(f'http://127.0.0.1:3000/jurnal/byidjurnal/{idJurnal}')
        if responseJurnal.status_code == 200:
            self.jurnal = json.loads(responseJurnal.text)
            
            self.idJurnal = idJurnal
            self.idTanaman = self.jurnal[0]["id_tanaman"]

            self.deskripsi_jurnal.setPlainText(self.jurnal[0]["deskripsi_jurnal"])
        else:
            self.jurnal = []
            print("No Jurnal Found")
    
    def setUpJurnalForm(self):
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
        self.header.setMinimumSize(QtCore.QSize(0, 60))
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
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main.setStyleSheet('''
                                #main {
                                    background-color: #F7F4D9;
                                }
                                ''')
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
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
        self.label_title_form.setText("Form Jurnal")
        self.label_title_form.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_4.addWidget(self.label_title_form, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_contents_1 = QtWidgets.QFrame(parent=self.main)
        self.frame_contents_1.setMaximumSize(QtCore.QSize(16777215, 320))
        self.frame_contents_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contents_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contents_1.setObjectName("frame_contents_1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_contents_1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.deskripsi_jurnal = QtWidgets.QTextEdit(parent=self.frame_contents_1)
        self.deskripsi_jurnal.setMinimumSize(QtCore.QSize(660, 300))
        self.deskripsi_jurnal.setMaximumSize(QtCore.QSize(660, 300))
        self.deskripsi_jurnal.setStyleSheet('''
                                            #deskripsi_jurnal {
                                                padding: 17px 17px;
                                                font-size: 14px;
                                                border-radius: 15px;
                                                background: #61876E;
                                                color: #F7F3D7;
                                                height: 40px;
                                                font-weight: 600;
                                                width: 243px;
                                            }
                                            ''')
        self.deskripsi_jurnal.setOverwriteMode(True)
        self.deskripsi_jurnal.setObjectName("deskripsi_jurnal")
        self.deskripsi_jurnal.setPlaceholderText(
            "Tulis jurnal kamu hari ini . . .")
        self.deskripsi_jurnal.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.deskripsi_jurnal.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.verticalLayout_9.addWidget(self.deskripsi_jurnal, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_contents_1)
        self.frame_description = QtWidgets.QFrame(parent=self.main)
        self.frame_description.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_description.setObjectName("frame_description")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_description)
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, -1)
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
        self.btn_submit.clicked.connect(self.validate_input)
        
        self.horizontalLayout_5.addWidget(self.btn_submit, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_description)
        self.verticalLayout.addWidget(self.main)
        self.setCentralWidget(self.centralwidget)

        self.btn_back.clicked.connect(self.on_btn_back_clicked)
    
    def clear_data(self):        
        self.deskripsi_jurnal.clear()
    
    def on_btn_back_clicked(self):
        self.clear_data()
        self.channel.emit("detail", self.idTanaman)
    
    def is_deskripsi_jurnal_null(self):
        return self.deskripsi_jurnal.toPlainText().strip() == ""
        
    def is_deskripsi_jurnal_too_long(self):
        return len(self.deskripsi_jurnal.toPlainText().strip()) > 255

    def validate_input(self):
        if self.is_deskripsi_jurnal_null():
            QMessageBox.warning(self, "Error", "Deskripsi jurnal tidak boleh kosong.")
        elif self.is_deskripsi_jurnal_too_long():
            QMessageBox.warning(self, "Error", "Panjang deskripsi tanaman tidak boleh lebih dari 255 karakter.")
        else :
            if (self.idJurnal == None): # Insert
                # masukin ke database dan balik ke data tanaman page
                data = {
                    "id_tanaman": self.idTanaman,
                    "deskripsi_jurnal": self.deskripsi_jurnal.toPlainText().strip()
                }
                response = requests.post(f'http://127.0.0.1:3000/jurnal/addjurnal', data=data)
                if response.status_code == 201:
                    print("Jurnal added successfully.")
                    self.clear_data()
                    self.channel.emit("detail", self.idTanaman)
                else:
                    print(f"Failed to add Jurnal. Status code: {response.status_code}")
            else: # Edit
                data = {
                    "deskripsi_jurnal": self.deskripsi_jurnal.toPlainText().strip()
                }
                response = requests.put(f'http://127.0.0.1:3000/jurnal/editjurnal/{self.idJurnal}', data=data)
                if response.status_code == 200:
                    print("Jurnal updated successfully.")
                    self.clear_data()
                    self.channel.emit("detail", self.todolist[0]["id_tanaman"])
                else:
                    print(f"Failed to update Jurnal. Status code: {response.status_code}")