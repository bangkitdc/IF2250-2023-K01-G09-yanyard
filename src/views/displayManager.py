from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon

# Windows
from views.windows.menuWindow import MenuWindow
from views.windows.artikelWindow import ArtikelWindow
from views.windows.detailTanamanWindow import DetailTanamanWindow
from views.windows.todolistWindow import TodolistWindow
from views.windows.dataTanamanWindow import DataTanamanWindow

# Forms
from views.forms.jurnalForm import JurnalForm
from views.forms.todolistForm import TodolistForm
from views.forms.tanamanForm import TanamanForm

class PageController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("yanyard - Main Menu")
        self.setWindowIcon(QIcon("assets\logo\logo.ico"))

        self.resize(960, 600)
        self.setUpPages()
        self.setUpListener()
        self.stackedWidget.show()

    def setUpPages(self):
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self)

        self.menuWindow = MenuWindow()
        self.artikelWindow = ArtikelWindow()
        self.todolistWindow = TodolistWindow()
        self.detailTanamanWindows = {}                          # Only indexing
        self.dataTanamanWindow = DataTanamanWindow()

        self.jurnalForm = JurnalForm()
        self.todolistForm = TodolistForm()
        self.tanamanForm = TanamanForm()

        # Add the windows to the stacked widget
        self.stackedWidget.addWidget(self.menuWindow)           # 0
        self.stackedWidget.addWidget(self.artikelWindow)        # 1
        self.stackedWidget.addWidget(self.todolistWindow)       # 2
        self.stackedWidget.addWidget(self.dataTanamanWindow)    # 3

        self.stackedWidget.addWidget(self.jurnalForm)           # 4
        self.stackedWidget.addWidget(self.todolistForm)         # 5
        self.stackedWidget.addWidget(self.tanamanForm)          # 6
        
        self.detailTanamanWindowsList = {}                      # The actual object
        self.setCentralWidget(self.stackedWidget)

    def setUpListener(self):
        self.menuWindow.channel.connect(self.handleMenuWindow)
        self.artikelWindow.channel.connect(self.handleArtikelWindow)
        self.todolistWindow.channel.connect(self.handleTodolistWindow)
        self.dataTanamanWindow.channel.connect(self.handleDataTanamanWindow)

        self.jurnalForm.channel.connect(self.handleJurnalForm)
        self.todolistForm.channel.connect(self.handleTodolistForm)
        self.tanamanForm.channel.connect(self.handleTanamanForm)

    def handleMenuWindow(self, page):
        if page == "artikel":
            self.setWindowTitle("yanyard - Artikel")
            self.stackedWidget.setCurrentIndex(1)
        elif page == "todolist":
            self.setWindowTitle("yanyard - To Do List")
            self.stackedWidget.setCurrentIndex(2)
        elif page == "data tanaman":
            self.setWindowTitle("yanyard - Data Tanaman")
            self.dataTanamanWindow.setUpDataTanamanWindow()
            self.stackedWidget.setCurrentIndex(3)
            
    def handleArtikelWindow(self, page):
        if page == "main":
            self.setWindowTitle("yanyard - Main Menu")
            self.stackedWidget.setCurrentIndex(0)

    def handleDetailTanamanWindow(self, page, idTanaman=None, idTDLOrJurnal=None):
        if page == "data tanaman":
            self.setWindowTitle("yanyard - Data Tanaman")
            self.dataTanamanWindow.setUpDataTanamanWindow()
            self.stackedWidget.setCurrentIndex(3)
        elif page == "form tanaman":
            self.setWindowTitle("yanyard - Tanaman Form")
            self.tanamanForm.setUpFields(idTanaman)
            self.stackedWidget.setCurrentIndex(6)
        elif page == "form tdl add":
            self.setWindowTitle("yanyard - To Do List Form")
            self.stackedWidget.setCurrentIndex(5)
            self.todolistForm.setUpFieldsAdd(idTanaman)
            self.todolistForm.setFromDetail()
        elif page == "form tdl edit":
            self.setWindowTitle("yanyard - To Do List Form")
            self.stackedWidget.setCurrentIndex(5)
            self.todolistForm.setUpFieldsEdit(idTDLOrJurnal)
            self.todolistForm.setFromDetail()
        elif page == "form jurnal add":
            self.setWindowTitle("yanyard - Jurnal Form")
            self.stackedWidget.setCurrentIndex(4)
            self.jurnalForm.setUpFieldsAdd(idTanaman)
        elif page == "form jurnal edit":
            self.setWindowTitle("yanyard - Jurnal Form")
            self.stackedWidget.setCurrentIndex(4)
            self.jurnalForm.setUpFieldsEdit(idTDLOrJurnal)
    
    def handleTodolistWindow(self, page, idTDL):
        if page == "main":
            self.setWindowTitle("yanyard - Main Menu")
            self.stackedWidget.setCurrentIndex(0)
        elif page == "form tdl edit":
            self.setWindowTitle("yanyard - To Do List Form")
            self.stackedWidget.setCurrentIndex(5)
            self.todolistForm.setUpFieldsEdit(idTDL)
            self.todolistForm.setFromMenu()
            
    def handleDataTanamanWindow(self, page, idTanaman=None):
        if page == "main":
            self.setWindowTitle("yanyard - Main Menu")
            self.stackedWidget.setCurrentIndex(0)
        elif page == "detail" and idTanaman != None:
            self.setWindowTitle("yanyard - Detail Tanaman")
            if idTanaman in self.detailTanamanWindows:
                self.stackedWidget.setCurrentIndex(
                    self.detailTanamanWindows[idTanaman])
            else:
                detailTanamanWindow = DetailTanamanWindow(idTanaman)
                self.detailTanamanWindows[idTanaman] = self.stackedWidget.addWidget(detailTanamanWindow)
                self.stackedWidget.setCurrentIndex(self.detailTanamanWindows[idTanaman])
                detailTanamanWindow.channel.connect(self.handleDetailTanamanWindow)
                self.detailTanamanWindowsList[idTanaman] = detailTanamanWindow
        elif page == "form tanaman":
            self.setWindowTitle("yanyard - Tanaman Form")
            self.stackedWidget.setCurrentIndex(6)

    def handleJurnalForm(self, page, idTanaman=None):
        if page == "detail":
            self.setWindowTitle("yanyard - Detail Tanaman")
            if idTanaman in self.detailTanamanWindows:
                self.stackedWidget.setCurrentIndex(self.detailTanamanWindows[idTanaman])
                print("halo")
                self.detailTanamanWindowsList[idTanaman].setUpDetailTanamanWindow()

    def handleTodolistForm(self, page, idTanaman=None):
        if page == "detail":
            self.setWindowTitle("yanyard - Detail Tanaman")
            if idTanaman in self.detailTanamanWindows:
                self.stackedWidget.setCurrentIndex(self.detailTanamanWindows[idTanaman])
                self.detailTanamanWindowsList[idTanaman].setUpDetailTanamanWindow()
        elif page == "tdl":
            self.setWindowTitle("yanyard - To Do List")
            self.stackedWidget.setCurrentIndex(2)

    def handleTanamanForm(self, page, idTanaman=None):
        if page == "data tanaman":
            self.setWindowTitle("yanyard - Data Tanaman")
            self.dataTanamanWindow.setUpDataTanamanWindow()
            self.stackedWidget.setCurrentIndex(3)
        elif page == "detail":
            self.setWindowTitle("yanyard - Detail Tanaman")
            if idTanaman in self.detailTanamanWindows:
                self.stackedWidget.setCurrentIndex(self.detailTanamanWindows[idTanaman])
                self.detailTanamanWindowsList[idTanaman].setUpDetailTanamanWindow()