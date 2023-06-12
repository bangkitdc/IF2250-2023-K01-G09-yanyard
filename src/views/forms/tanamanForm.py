from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QGuiApplication, QFontDatabase
from PyQt6.QtCore import Qt, pyqtSignal
import os, pathlib, requests, json, re, shutil

class TanamanForm(QMainWindow):
    channel = pyqtSignal(str, int)

    def __init__(self, idTanaman=None):
        super().__init__()
        self.idTanaman = idTanaman
        self.setUpTanamanForm()
        
    def setUpFields(self, idTanaman):
        responseDetail = requests.get(f'http://127.0.0.1:3000/tanaman/{idTanaman}')
        if responseDetail.status_code == 200:
            self.detailTanaman = json.loads(responseDetail.text)
            
            self.idTanaman = idTanaman
            self.nama_tanaman.setPlainText(self.detailTanaman[0]["nama_tanaman"])
            self.deskripsi_tanaman.setPlainText(self.detailTanaman[0]["deskripsi_tanaman"])
            
            self.image_tanaman = self.detailTanaman[0]["gambar"]
            
            if self.image_tanaman == None or not os.path.isfile(self.image_tanaman):
                pass
            else:
                self.widget_img.setStyleSheet(
                        f"#widget_img {{border-image: url({self.image_tanaman}) 0 0 0 0 stretch stretch; background-attachment: fixed; border-radius:40px;}}")

        else:
            self.detailTanaman = []
            print("No Detail Tanaman Found")

    def setUpTanamanForm(self):
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
        
        if (self.idTanaman != None):
            self.setUpFields(self.idTanaman)

    def initializeWidgets(self, path):
        self.setStyleSheet('''
                                *{
                                    border: none;
                                    padding: 0;
                                    margin: 0;
                                    font-family: Poppins;
                                }
                                
                                QScrollBar:vertical {
                                    background-color: transparent;
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
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(parent=self.centralwidget)
        self.header.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
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
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
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
        self.label_title_form.setText("Form Tanaman")
        self.label_title_form.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.horizontalLayout_4.addWidget(self.label_title_form, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_contents_1 = QtWidgets.QFrame(parent=self.main)
        self.frame_contents_1.setMinimumSize(QtCore.QSize(500, 340))
        self.frame_contents_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_contents_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_contents_1.setObjectName("frame_contents_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_contents_1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_3.setMinimumSize(QtCore.QSize(180, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(180, 210))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_img = QtWidgets.QPushButton(parent=self.frame_3)
        self.widget_img.setMinimumSize(QtCore.QSize(160, 200))
        self.widget_img.setMaximumSize(QtCore.QSize(160, 200))
        
        self.image_tanaman = None
        image = "assets/images/tanaman/add_photo.png"
        self.widget_img.setStyleSheet(f'''
                                        #widget_img {{
                                            border-image: url({image}) 0 0 0 0 stretch stretch;
                                            border-radius:40px;
                                        }}
                                        ''')
        
        self.widget_img.setObjectName("widget_img")
        self.widget_img.setCursor(Qt.CursorShape.PointingHandCursor)
        self.widget_img.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        
        self.verticalLayout_4.addWidget(self.widget_img, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame_2.setMaximumSize(QtCore.QSize(370, 55))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nama_tanaman = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        self.nama_tanaman.setMinimumSize(QtCore.QSize(310, 45))
        self.nama_tanaman.setMaximumSize(QtCore.QSize(16777215, 45))
        self.nama_tanaman.setStyleSheet('''
                                        #nama_tanaman {
                                            padding: 7px 12px;
                                            border-radius: 20px;
                                            background: #61876E;
                                            color: #F7F3D7;
                                            font-size: 14px;
                                            font-weight: 600;
                                        }
                                        ''')
        self.nama_tanaman.setMaximumBlockCount(1)
        self.nama_tanaman.setObjectName("nama_tanaman")
        self.nama_tanaman.setPlaceholderText("Masukkan nama tanamanmu . . .")
        self.nama_tanaman.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.verticalLayout_5.addWidget(self.nama_tanaman, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame = QtWidgets.QFrame(parent=self.frame_contents_1)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(9, 4, 9, 4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.deskripsi_tanaman = QtWidgets.QPlainTextEdit(parent=self.frame)
        self.deskripsi_tanaman.setMinimumSize(QtCore.QSize(310, 40))
        self.deskripsi_tanaman.setStyleSheet('''
                                            #deskripsi_tanaman {
                                                padding: 12px;
                                                font-size: 14px;
                                                border-radius: 15px;
                                                background: #61876E;
                                                color: #F7F3D7;
                                                font-weight: 600;
                                            }
                                            ''')
        self.deskripsi_tanaman.setOverwriteMode(True)
        self.deskripsi_tanaman.setObjectName("deskripsi_tanaman")
        self.deskripsi_tanaman.setPlaceholderText("Ceritakan tentang tanamanmu. . .")
        self.deskripsi_tanaman.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=12, xOffset=0, yOffset=0))
        
        self.verticalLayout_6.addWidget(self.deskripsi_tanaman)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_contents_1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_description = QtWidgets.QFrame(parent=self.main)
        self.frame_description.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_description.setObjectName("frame_description")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_description)
        self.horizontalLayout_5.setContentsMargins(-1, 4, -1, 4)
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
        self.widget_img.clicked.connect(self.on_img_clicked)
        
    def clear_data(self):
        self.nama_tanaman.clear()
        self.deskripsi_tanaman.clear()
        self.image_tanaman = ""
        image = "assets/images/tanaman/add_photo.png"
        self.widget_img.setStyleSheet(f'''
                                        #widget_img {{
                                            border-image: url({image}) 0 0 0 0 stretch stretch;
                                            border-radius:40px;
                                        }}
                                        ''')

    def on_btn_back_clicked(self):
        self.clear_data()
        if (not self.fromDetailTanaman):
            self.channel.emit("tdl", None)
        else:
            self.channel.emit("detail", self.idTanaman)
        
    def on_img_clicked(self):
        # Open File Dialog
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.xpm *.jpg *.jpeg)')
        if file_path:
            self.image_tanaman = file_path
            self.widget_img.setStyleSheet(f'''
                                            #widget_img {{
                                                border-image: url({self.image_tanaman}) 0 0 0 0 stretch stretch;
                                                border-radius:40px;
                                            }}
                                            ''')
    
    def is_nama_tanaman_null(self):
        return self.nama_tanaman.toPlainText().strip() == ""
    
    def is_nama_tanaman_too_long(self):
        return len(self.nama_tanaman.toPlainText().strip()) > 50
    
    def is_deskripsi_tanaman_too_long(self):
        return len(self.deskripsi_tanaman.toPlainText().strip()) > 255

    def validate_input(self):
        if not self.is_nama_tanaman_null() and not self.is_nama_tanaman_too_long() and not self.is_deskripsi_tanaman_too_long():
            dir_path = "assets/images/tanaman"
            num_regex = re.compile(r"^\d+")
            max_num = 0
            
            for filename in os.listdir(dir_path):
                # Check if the filename matches the "*.png" pattern and starts with a number
                if filename.endswith(".png") and num_regex.match(filename):
                    num = int(num_regex.match(filename).group())

                    if num > max_num:
                        max_num = num
            
            imageFormat = f"assets/images/tanaman/{max_num + 1}.png"
            
            if (self.idTanaman == None): # Insert
                if self.image_tanaman == None:
                    imageFormat = None
                # masukin ke database dan balik ke data tanaman page
                data = {
                    "nama_tanaman": self.nama_tanaman.toPlainText().strip(),
                    "deskripsi_tanaman": self.deskripsi_tanaman.toPlainText().strip(),
                    "gambar": imageFormat
                }
                response = requests.post(f'http://127.0.0.1:3000/tanaman/addtanaman', data=data)
                if response.status_code == 201:
                    if (self.image_tanaman != None):
                        shutil.copyfile(self.image_tanaman, imageFormat)
                    print("Tanaman added successfully.")
                    self.clear_data()
                    self.channel.emit("data tanaman", None)
                else:
                    print(f"Failed to add Tanaman. Status code: {response.status_code}")
            else: # Edit
                img = self.image_tanaman
                file_name = os.path.basename(img)
                dir_path = "assets/images/tanaman"
                
                if not os.path.exists(os.path.join(dir_path, file_name)):
                    img = imageFormat
                
                data = {
                    "nama_tanaman": self.nama_tanaman.toPlainText().strip(),
                    "deskripsi_tanaman": self.deskripsi_tanaman.toPlainText().strip(),
                    "gambar": img
                }
                response = requests.put(f'http://127.0.0.1:3000/tanaman/edittanaman/{self.idTanaman}', data=data)
                if response.status_code == 200:
                    if (self.image_tanaman != img):
                        shutil.copyfile(self.image_tanaman, img)
                    print("Tanaman updated successfully.")
                    self.clear_data()
                    self.channel.emit("detail", self.idTanaman)
                else:
                    print(f"Failed to update Tanaman. Status code: {response.status_code}")
        else :
            if self.is_nama_tanaman_null():
                QMessageBox.warning(self, "Error", "Nama tanaman tidak boleh kosong.")
            elif self.is_nama_tanaman_too_long():
                QMessageBox.warning(self, "Error", "Panjang nama tanaman tidak boleh lebih dari 50 karakter.")
            elif self.is_deskripsi_tanaman_too_long():
                QMessageBox.warning(self, "Error", "Panjang deskripsi tanaman tidak boleh lebih dari 255 karakter.")

        
