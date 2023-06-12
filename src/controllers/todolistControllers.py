from flask import jsonify, request

from models.todolistModels import TodolistModels


class TodolistControllers:
    @staticmethod
    def getTodolist():
        try:
            fetchedData = TodolistModels.getAllTodolist()

            if fetchedData is None:
                return "No Todolist Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tdl": d.getIDTDL(),
                                "id_tanaman": d.getIDTanaman(),
                                "waktu": d.getWaktuTDL(),
                                "deskripsi_tdl": d.getDeskripsiTDL()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def getTodolistByIdTanaman(idTanaman):
        try:
            fetchedData = TodolistModels.getTodolistByIdTanaman(idTanaman)

            if fetchedData is None:
                return "No Todolist Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tdl": d.getIDTDL(),
                                "id_tanaman": d.getIDTanaman(),
                                "waktu": d.getWaktuTDL(),
                                "deskripsi_tdl": d.getDeskripsiTDL()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400
    
    @staticmethod
    def getTodolistByIdTDL(idTDL):
        try:
            fetchedData = TodolistModels.getTodolistByIdTDL(idTDL)

            if fetchedData is None:
                return "No Todolist Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tdl": d.getIDTDL(),
                                "id_tanaman": d.getIDTanaman(),
                                "waktu": d.getWaktuTDL(),
                                "deskripsi_tdl": d.getDeskripsiTDL()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def deleteTodolistByIdTDL(idTDL):
        try:
            TodolistModels.deleteTodolist(idTDL)

            return "To Do List Successfully Deleted", 204

        except Exception as e:
            return str(e), 400
        
    @staticmethod
    def postTodolist():
        try:
            id_tanaman = request.form.get("id_tanaman")
            waktu = request.form.get("waktu")
            deskripsi_tdl = request.form.get("deskripsi_tdl")
                        
            TodolistModels(id_tdl=None, id_tanaman=id_tanaman, waktu=waktu, deskripsi_tdl=deskripsi_tdl)
            
            return "Created", 201

        except Exception as e:
            return str(e), 400
        
    @staticmethod
    def editTodolist(idTDL):
        try:
            waktu = request.form.get("waktu")
            deskripsi_tdl = request.form.get("deskripsi_tdl")
            
            TodolistModels.editTodolist(idTDL, waktu, deskripsi_tdl)
            
            return "OK", 200

        except Exception as e:
            return str(e), 400
