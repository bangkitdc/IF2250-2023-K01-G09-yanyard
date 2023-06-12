from flask import Blueprint
from controllers.tanamanControllers import TanamanControllers

tanamanRoutes = Blueprint("tanamanRoutes", __name__)

@tanamanRoutes.route("/", methods=["GET"])
def get_tanamans():
    return TanamanControllers.getTanaman()

@tanamanRoutes.route("/<int:idTanaman>", methods=["GET"])
def get_tanaman(idTanaman):
    return TanamanControllers.getTanamanById(idTanaman)

@tanamanRoutes.route("/deletetanaman/<int:idTanaman>", methods=["DELETE"])
def delete_tanaman(idTanaman):
    return TanamanControllers.deleteTanamanByIdTanaman(idTanaman)

@tanamanRoutes.route("/addtanaman", methods=["POST"])
def post_tanaman():
    return TanamanControllers.postTanaman()

@tanamanRoutes.route("/edittanaman/<int:idTanaman>", methods=["PUT"])
def edit_tanaman(idTanaman):
    return TanamanControllers.editTanaman(idTanaman)