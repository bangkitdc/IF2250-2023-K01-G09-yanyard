from flask import Blueprint

mainRoutes = Blueprint('main', __name__)

@mainRoutes.route('/')
def index():
    return 'Server is running on port 3000'
