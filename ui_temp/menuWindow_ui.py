# Form implementation generated from reading ui file 'd:\STEI\Jurusan\Semester-4\RPL\Tubes\if2250-2023-k01-g09-yanyard\ui_temp\menuWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#header {\n"
"    background-color: #3C6255;\n"
"}\n"
"\n"
"#main {\n"
"    background-color: #F7F4D9;\n"
"}\n"
"\n"
"#footer {\n"
"    background-color: #F7F4D9;\n"
"}\n"
"\n"
"QPushButton {\n"
"    padding: 5px 10px;\n"
"    border-radius: 25px;\n"
"    background: #3C6255;\n"
"    color: #F7F3D7;\n"
"    height: 40px;\n"
"    width: 243px;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #23493C;\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.logo.setPixmap(QtGui.QPixmap("d:\\STEI\\Jurusan\\Semester-4\\RPL\\Tubes\\if2250-2023-k01-g09-yanyard\\ui_temp\\printilan logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.main = QtWidgets.QWidget(parent=self.centralwidget)
        self.main.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        self.logo_2.setPixmap(QtGui.QPixmap("d:\\STEI\\Jurusan\\Semester-4\\RPL\\Tubes\\if2250-2023-k01-g09-yanyard\\ui_temp\\logo yanyard.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName("logo_2")
        self.horizontalLayout_4.addWidget(self.logo_2)
        self.verticalLayout_2.addWidget(self.frame_logo_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_btn = QtWidgets.QFrame(parent=self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btn.sizePolicy().hasHeightForWidth())
        self.frame_btn.setSizePolicy(sizePolicy)
        self.frame_btn.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_btn.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_btn.setObjectName("frame_btn")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_btn)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_tanaman = QtWidgets.QFrame(parent=self.frame_btn)
        self.frame_tanaman.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tanaman.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tanaman.setObjectName("frame_tanaman")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_tanaman)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_tanaman = QtWidgets.QPushButton(parent=self.frame_tanaman)
        self.btn_tanaman.setMouseTracking(True)
        self.btn_tanaman.setStyleSheet("")
        self.btn_tanaman.setDefault(False)
        self.btn_tanaman.setFlat(False)
        self.btn_tanaman.setObjectName("btn_tanaman")
        self.verticalLayout_4.addWidget(self.btn_tanaman, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_tanaman)
        self.frame_tdl = QtWidgets.QFrame(parent=self.frame_btn)
        self.frame_tdl.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_tdl.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_tdl.setObjectName("frame_tdl")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_tdl)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_tdl = QtWidgets.QPushButton(parent=self.frame_tdl)
        self.btn_tdl.setStyleSheet("")
        self.btn_tdl.setDefault(False)
        self.btn_tdl.setFlat(False)
        self.btn_tdl.setObjectName("btn_tdl")
        self.verticalLayout_5.addWidget(self.btn_tdl, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_tdl)
        self.frame_artikel = QtWidgets.QFrame(parent=self.frame_btn)
        self.frame_artikel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_artikel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_artikel.setObjectName("frame_artikel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_artikel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_artikel = QtWidgets.QPushButton(parent=self.frame_artikel)
        self.btn_artikel.setStyleSheet("")
        self.btn_artikel.setDefault(False)
        self.btn_artikel.setFlat(False)
        self.btn_artikel.setObjectName("btn_artikel")
        self.verticalLayout_6.addWidget(self.btn_artikel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_artikel)
        self.verticalLayout_2.addWidget(self.frame_btn)
        self.verticalLayout.addWidget(self.main)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_tanaman.setText(_translate("MainWindow", "Data Tanaman"))
        self.btn_tdl.setText(_translate("MainWindow", "To Do List"))
        self.btn_artikel.setText(_translate("MainWindow", "Artikel"))
