from flask import Blueprint
from controllers.artikelControllers import ArtikelControllers

artikelRoutes = Blueprint("artikelRoutes", __name__)

@artikelRoutes.route("/", methods=["GET"])
def get_artikels():
    return ArtikelControllers.getArtikel()