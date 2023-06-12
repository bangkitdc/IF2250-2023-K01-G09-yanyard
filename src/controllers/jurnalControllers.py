from flask import jsonify, request

from models.jurnalModels import JurnalModels


class JurnalControllers:
    @staticmethod
    def getJurnal():
        try:
            fetchedData = JurnalModels.getAllJurnal()

            if fetchedData is None:
                return "No Jurnal Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_jurnal": d.getIDJurnal(),
                                "id_tanaman": d.getIDTanaman(),
                                "tanggal_jurnal": d.getTanggalJurnal(),
                                "deskripsi_jurnal": d.getDeskripsiJurnal()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def getJurnalByIdTanaman(idTanaman):
        try:
            fetchedData = JurnalModels.getJurnalByIdTanaman(idTanaman)

            if fetchedData is None:
                return "No Jurnal Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_jurnal": d.getIDJurnal(),
                                "id_tanaman": d.getIDTanaman(),
                                "tanggal_jurnal": d.getTanggalJurnal(),
                                "deskripsi_jurnal": d.getDeskripsiJurnal()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400
        
    @staticmethod
    def getJurnalByIdJurnal(idJurnal):
        try:
            fetchedData = JurnalModels.getJurnalByIdJurnal(idJurnal)

            if fetchedData is None:
                return "No Jurnal Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_jurnal": d.getIDJurnal(),
                                "id_tanaman": d.getIDTanaman(),
                                "tanggal_jurnal": d.getTanggalJurnal(),
                                "deskripsi_jurnal": d.getDeskripsiJurnal()})

                return jsonify(res), 200

        except Exception as e:
            return str(e), 400

    @staticmethod
    def deleteJurnalByIdJurnal(idJurnal):
        try:
            JurnalModels.deleteJurnal(idJurnal)

            return "Jurnal Successfully Deleted", 204

        except Exception as e:
            return str(e), 400
        
    @staticmethod
    def postJurnal():
        try:
            id_tanaman = request.form.get("id_tanaman")
            deskripsi_jurnal = request.form.get("deskripsi_jurnal")

            JurnalModels(id_jurnal=None, id_tanaman=id_tanaman, tanggal_jurnal=None, deskripsi_jurnal=deskripsi_jurnal)

            return "Created", 201

        except Exception as e:
            return str(e), 400

    @staticmethod
    def editJurnal(idJurnal):
        try:
            deskripsi_jurnal = request.form.get("deskripsi_jurnal")

            JurnalModels.editJurnal(idJurnal, deskripsi_jurnal)

            return "OK", 200

        except Exception as e:
            return str(e), 400
