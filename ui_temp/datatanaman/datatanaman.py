# Form implementation generated from reading ui file 'y.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 610)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"

"#label_title_data {\n"
"    color: #F7F4D9;\n"
"    background-color: #3C6255;\n"
"    padding: 15px 58px;\n"
"    border-radius: 25px;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"}\n"

"#header {\n"
"    background-color: #3C6255;\n"
"}\n")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.header_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.header_2.setGeometry(QtCore.QRect(0, 0, 960, 60))
        self.header_2.setMinimumSize(QtCore.QSize(0, 60))
        self.header_2.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_temp = QtWidgets.QFrame(parent=self.header_2)
        self.frame_temp.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp.setObjectName("frame_temp")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_temp)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_back = QtWidgets.QPushButton(parent=self.frame_temp)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/left__arrow2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(24, 24))
        self.btn_back.setAutoExclusive(False)
        self.btn_back.setFlat(False)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_2.addWidget(self.frame_temp)
        self.frame_logo = QtWidgets.QFrame(parent=self.header_2)
        self.frame_logo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logo = QtWidgets.QLabel(parent=self.frame_logo)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setMaximumSize(QtCore.QSize(42, 42))
        self.logo.setPixmap(QtGui.QPixmap("../artikel/logo_circle.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_5.addWidget(self.logo)
        self.horizontalLayout_2.addWidget(self.frame_logo)
        self.frame_temp_2 = QtWidgets.QFrame(parent=self.header_2)
        self.frame_temp_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_temp_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_temp_2.setObjectName("frame_temp_2")
        self.horizontalLayout_2.addWidget(self.frame_temp_2)
        
        
        # self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        # self.scrollArea.setGeometry(QtCore.QRect(-1, 60, 961, 550))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 959, 600))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
         
#         self.main = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
#         self.main.setSizePolicy(sizePolicy)
#         self.main.setStyleSheet("#main {\n"
# "    background-color: #F7F4D9;\n"
# "}")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-1, 60, 961, 550))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 959, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(400, 100, 300, 60))
        self.frame.setObjectName("frame")
        # self.frame.setStyleSheet("background-color: #61876E;\n")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setSpacing(0)
        # add the frame to the vertical layout of the scrollAreaWidgetContents
        self.widget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 961, 531))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(0)
        
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.label_title_data = QtWidgets.QLabel(parent=self.frame)
        self.label_title_data.setObjectName("label_title_data")
        
        self.label_title_data.setGeometry(QtCore.QRect(325, 0, 250, 60))
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(960, 400))
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 100, 961, 400))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        # self.gridLayoutWidget.setStyleSheet("background-color: black;")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        # Add a new column to the right
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(1, 1)  # new column
        if self.gridLayout.count() >= 6:
            self.verticalLayout_2.resize(self.scrollAreaWidgetContents.width(), self.gridLayout.sizeHint().height())
            # self.scrollArea = QtWidgets.QScrollArea()
            self.scrollArea.setWidgetResizable(True)
            self.scrollWidget = QtWidgets.QWidget()
            self.scrollWidget.setLayout(self.gridLayoutWidget)
            self.scrollArea.setWidget(self.scrollWidget)

            # Add the scroll area to the main layout
            self.centralwidget.addWidget(self.scrollArea)

            # Create a new widget to hold the frames inside the scroll area
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addLabel)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(160, 40))
        
        self.pushButton.setGeometry(QtCore.QRect(750, 480, 160, 40))
        self.pushButton.setStyleSheet("#pushButton{\n"
"    color: #F7F4D9;\n"
"    background-color: #61876E;\n"
"    padding: 10px;\n"
"    border-radius: 20px;\n"
"    font-size: 14px;\n"
"    font-weight: 800;\n"
"}")

        # self.verticalLayout.addWidget(self.pushButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.scrollArea.setStyleSheet("#scrollArea {\n"
"    background-color: #F7F4D9;}\n")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", " Kembali"))
        self.label_title_data.setText(_translate("MainWindow", "Data Tanaman"))
        self.pushButton.setText(_translate("MainWindow", "Add Tanaman"))
    
    def addLabel(self):
        frame = QtWidgets.QFrame()
        frame.setContentsMargins(0, 0, 0, 0)  
        frame.setStyleSheet("QFrame { max-width=170px;}") 
        frame.setFixedSize(320,200)
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(frame)
        layout = QtWidgets.QVBoxLayout(frame)
        
        name_label = QtWidgets.QLabel(f"Tanaman {self.gridLayout.count() + 1}")
        name_label.setStyleSheet("color: #3C6255;margin-top:5px; font-size:20px; font-weight:600;")
        name_layout = QtWidgets.QHBoxLayout()
        name_layout.addWidget(name_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        image_label = QtWidgets.QLabel()
        image_label.setPixmap(QtGui.QPixmap("tanaman/cabai.jpg"))
        image_label.setFixedSize(110, 120) 
        image_label.setStyleSheet(" margin-top: 5px; margin-bottom: 5px; border-radius: 18px;")
        image_label.setStyleSheet("#image_label {\n"
"    border-radius: 5px;\n"     
 "}\n")
        image_layout = QtWidgets.QHBoxLayout()
        image_layout.addWidget(image_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        
        waktu_label = QtWidgets.QLabel("since April 2022")
        waktu_label.setStyleSheet("color: #61876E; margin-top: 5px; font-size:11px; font-weight:300;")
        waktu_layout = QtWidgets.QHBoxLayout()
        waktu_layout.addWidget(waktu_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        layout.addLayout(name_layout)
        layout.addSpacing(5) # Add some vertical spacing
        layout.addLayout(image_layout)
        layout.addSpacing(5) # Add some vertical spacing
        layout.addLayout(waktu_layout)
        layout.addStretch() # Add some stretch at the bottom to make the layout expandable
        
        # if self.verticalLayout.count() > 6:
        #     self.scrollAreaWidgetContents.resize(self.scrollAreaWidgetContents.width(), self.verticalLayout.sizeHint().height())
            
        self.gridLayout.addWidget(frame, self.gridLayout.count() // 3, self.gridLayout.count() % 3)
        
    def onImageLabelClicked(self):
        #kalo gambarnya ke click bisa do something here
        pass


# class ClickableImageLabel(QtWidgets.QLabel):
#     clicked = QtCore.pyqtSignal()  # Create a custom signal

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setCursor(QtCore.Qt.PointingHandCursor)  # Set the cursor to a hand cursor

#     def mousePressEvent(self, event):
#         self.clicked.emit()  # Emit the custom signal when the label is clicked
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())   
