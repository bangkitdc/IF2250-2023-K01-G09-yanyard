from flask import Blueprint
from controllers.todolistControllers import TodolistControllers

todolistRoutes = Blueprint("todolistRoutes", __name__)

@todolistRoutes.route("/", methods=["GET"])
def get_todolists():
    return TodolistControllers.getTodolist()

@todolistRoutes.route("/byidtanaman/<int:idTanaman>", methods=["GET"])
def get_todolist_by_idtanaman(idTanaman):
    return TodolistControllers.getTodolistByIdTanaman(idTanaman)

@todolistRoutes.route("/byidtodolist/<int:idTDL>", methods=["GET"])
def get_todolist_by_idtdl(idTDL):
    return TodolistControllers.getTodolistByIdTDL(idTDL)

@todolistRoutes.route("/deletetodolist/<int:idTDL>", methods=["DELETE"])
def delete_todolist(idTDL):
    return TodolistControllers.deleteTodolistByIdTDL(idTDL)

@todolistRoutes.route("/addtodolist", methods=["POST"])
def post_todolist():
    return TodolistControllers.postTodolist()

@todolistRoutes.route("/edittodolist/<int:idTDL>", methods=["PUT"])
def edit_todolist(idTDL):
    return TodolistControllers.editTodolist(idTDL)