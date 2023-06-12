from flask import jsonify, request

from models.artikelModels import ArtikelModels

class ArtikelControllers:
    @staticmethod
    def getArtikel():
        try:
            fetchedData = ArtikelModels.getAllArtikel()
                        
            if fetchedData is None:
                return "No Artikel Found", 404
            else:
                res = []
                for d in fetchedData:
                    res.append({"id_artikel": d.getIDArtikel(),
                                "judul": d.getJudulArtikel(),
                                "isi_artikel": d.getIsiArtikel(),
                                "gambar": d.getGambarArtikel()})
                    
                return jsonify(res), 200
                
        except Exception as e:
            return str(e), 400