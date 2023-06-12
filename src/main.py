import sys
from PyQt6.QtWidgets import QApplication
from threading import Thread

from app import app
from views import displayManager

from routes.mainRoutes import mainRoutes
from routes.artikelRoutes import artikelRoutes
from routes.tanamanRoutes import tanamanRoutes
from routes.todolistRoutes import todolistRoutes
from routes.jurnalRoutes import jurnalRoutes

def initServer():
    # Backend
    app.register_blueprint(mainRoutes, url_prefix = "/")
    app.register_blueprint(artikelRoutes, url_prefix = "/artikel")
    app.register_blueprint(tanamanRoutes, url_prefix = "/tanaman")
    app.register_blueprint(todolistRoutes, url_prefix = "/todolist")
    app.register_blueprint(jurnalRoutes, url_prefix = "/jurnal")
    
    app.run(port=3000, use_reloader=False)

if __name__ == '__main__':
    threadBackend = Thread(target=initServer)
    threadBackend.daemon = True
    threadBackend.start()
    
    window = QApplication(sys.argv)
    view = displayManager.PageController()
    view.show()
    sys.exit(window.exec())