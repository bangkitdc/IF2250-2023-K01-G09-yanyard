from flask import jsonify, request

from models.tanamanModels import TanamanModels


class TanamanControllers:
    @staticmethod
    def getTanaman():
        try:
            fetchedData = TanamanModels.getAllTanaman()

            if fetchedData is None:
                return "No Tanaman Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tanaman": d.getIDTanaman(),
                                "nama_tanaman": d.getNamaTanaman(),
                                "tanggal_tanaman": d.getTanggalTanaman(),
                                "deskripsi_tanaman": d.getDeskripsiTanaman(),
                                "gambar": d.getGambarTanaman()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def getTanamanById(id):
        try:
            fetchedData = TanamanModels.getTanaman(id)

            if fetchedData is None:
                return "No Tanaman Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_tanaman": d.getIDTanaman(),
                                "nama_tanaman": d.getNamaTanaman(),
                                "tanggal_tanaman": d.getTanggalTanaman(),
                                "deskripsi_tanaman": d.getDeskripsiTanaman(),
                                "gambar": d.getGambarTanaman()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def postTanaman():
        try:
            nama_tanaman = request.form.get("nama_tanaman")
            deskripsi_tanaman = request.form.get("deskripsi_tanaman")
            gambar = request.form.get("gambar")
            
            TanamanModels(id_tanaman=None, nama_tanaman=nama_tanaman, tanggal_tanaman=None, deskripsi_tanaman=deskripsi_tanaman, gambar=gambar)
            
            return "Created", 201

        except Exception as e:
            return str(e), 400
    
    @staticmethod
    def deleteTanamanByIdTanaman(idTanaman):
        try:
            TanamanModels.deleteTanaman(idTanaman)

            return "Tanaman Successfully Deleted", 204

        except Exception as e:
            return str(e), 400
        
    @staticmethod
    def editTanaman(idTanaman):
        try:
            nama_tanaman = request.form.get("nama_tanaman")
            deskripsi_tanaman = request.form.get("deskripsi_tanaman")
            gambar = request.form.get("gambar")
            
            TanamanModels.editTanaman(idTanaman, nama_tanaman, deskripsi_tanaman, gambar)
            
            return "OK", 200

        except Exception as e:
            return str(e), 400