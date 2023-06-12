from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ToDoListWindow(object):
    def setupUi(self, ToDoListWindow):
        ToDoListWindow.setObjectName("ToDoListWindow")
        ToDoListWindow.setEnabled(True)
        ToDoListWindow.resize(960, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ToDoListWindow.sizePolicy().hasHeightForWidth())
        ToDoListWindow.setSizePolicy(sizePolicy)
        ToDoListWindow.setMinimumSize(QtCore.QSize(0, 0))
        ToDoListWindow.setAutoFillBackground(True)
        ToDoListWindow.setStyleSheet("*{\n"
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
"}")
        ToDoListWindow.setSizeGripEnabled(True)
        self.header = QtWidgets.QWidget(parent=ToDoListWindow)
        self.header.setEnabled(True)
        self.header.setGeometry(QtCore.QRect(0, 0, 960, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.header.setAutoFillBackground(False)
        self.header.setObjectName("header")
        self.frame_logo = QtWidgets.QFrame(parent=self.header)
        self.frame_logo.setGeometry(QtCore.QRect(459, 9, 42, 42))
        self.frame_logo.setObjectName("frame_logo")
        self.footer = QtWidgets.QWidget(parent=ToDoListWindow)
        self.footer.setEnabled(False)
        self.footer.setGeometry(QtCore.QRect(0, 540, 960, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.footer.setAutoFillBackground(False)
        self.footer.setStyleSheet("#footer {\n"
"    background-color: #F7F4D9;\n"
"}")
        self.footer.setObjectName("footer")
        self.frame = QtWidgets.QFrame(parent=self.footer)
        self.frame.setGeometry(QtCore.QRect(0, 540, 960, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.body = QtWidgets.QWidget(parent=ToDoListWindow)
        self.body.setGeometry(QtCore.QRect(0, 60, 960, 480))
        self.body.setStyleSheet("#body {\n"
"    background-color: #F7F4D9;\n"
"}")
        self.body.setObjectName("body")
        self.content = QtWidgets.QFrame(parent=self.body)
        self.content.setGeometry(QtCore.QRect(-1, 9, 961, 471))
        self.content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.submit = QtWidgets.QFrame(parent=self.content)
        self.submit.setGeometry(QtCore.QRect(0, 310, 961, 80))
        self.submit.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.submit.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.submit.setObjectName("submit")
        self.btn_submit = QtWidgets.QPushButton(parent=self.submit)
        self.btn_submit.setGeometry(QtCore.QRect(390, 10, 181, 31))
        self.btn_submit.setStyleSheet("QPushButton {\n"
"    padding: 5px 10px;\n"
"    border-radius: 15px;\n"
"    background: #3C6255;\n"
"    color: #F7F3D7;\n"
"    height: 40px;\n"
"    width: 243px;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #23493C;\n"
"}")
        self.btn_submit.setDefault(False)
        self.btn_submit.setFlat(False)
        self.btn_submit.setObjectName("btn_submit")
        self.deskripsi = QtWidgets.QFrame(parent=self.content)
        self.deskripsi.setGeometry(QtCore.QRect(0, 180, 961, 131))
        self.deskripsi.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.deskripsi.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.deskripsi.setObjectName("deskripsi")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.deskripsi)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 20, 331, 41))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    padding: 7px 10px;\n"
"    border-radius: 15px;\n"
"    background: #61876E;\n"
"    color: #F7F3D7;\n"
"    height: 40px;\n"
"    width: 243px;\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    background-color: #23493C;\n"
"}\n"
"")
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.plainTextEdit.setMidLineWidth(0)
        self.plainTextEdit.setMaximumBlockCount(1)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.frame_2 = QtWidgets.QFrame(parent=self.content)
        self.frame_2.setGeometry(QtCore.QRect(-1, 90, 961, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=self.frame_2)
        self.dateTimeEdit.setGeometry(QtCore.QRect(380, 50, 201, 31))
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit {\n"
"    padding: 7px 10px;\n"
"    border-radius: 15px;\n"
"    background: #61876E;\n"
"    color: #F7F3D7;\n"
"    height: 40px;\n"
"    width: 243px;\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QDateTimeEdit:hover {\n"
"    background-color: #23493C;\n"
"}\n"
"")
        self.dateTimeEdit.setTime(QtCore.QTime(1, 0, 0))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.Section.YearSection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setCurrentSectionIndex(2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.retranslateUi(ToDoListWindow)
        QtCore.QMetaObject.connectSlotsByName(ToDoListWindow)

    def retranslateUi(self, ToDoListWindow):
        _translate = QtCore.QCoreApplication.translate
        ToDoListWindow.setWindowTitle(_translate("ToDoListWindow", "Dialog"))
        self.btn_submit.setText(_translate("ToDoListWindow", "Submit"))
        self.plainTextEdit.setPlainText(_translate("ToDoListWindow", "Tulis Deskripsi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToDoListWindow = QtWidgets.QDialog()
    ui = Ui_ToDoListWindow()
    ui.setupUi(ToDoListWindow)
    ToDoListWindow.show()
    sys.exit(app.exec())
