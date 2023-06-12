from models.db import mysql

class ArtikelModels:
    def __init__(self, id_artikel, judul, isi_artikel, gambar):
        self.id_artikel = id_artikel
        self.judul = judul
        self.isi_artikel = isi_artikel
        self.gambar = gambar
    
    @classmethod
    def getAllArtikel(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM artikel")
        
        dataArtikel = cursor.fetchall()
        
        # If empty set
        if len(dataArtikel) == 0:
            cursor.close()
            return None
        else:
            listArtikel = []
            for data in dataArtikel:
                id_artikel, judul, isi_artikel, gambar = data
                
                # initialize class
                self = cls.__new__(cls)
                self.id_artikel = id_artikel
                self.judul = judul
                self.isi_artikel = isi_artikel
                self.gambar = gambar
                
                listArtikel.append(self)
            
            cursor.close()
            return listArtikel
        
    def getIDArtikel(self):
        return self.id_artikel
    
    def getJudulArtikel(self):
        return self.judul
    
    def getIsiArtikel(self):
        return self.isi_artikel
    
    def getGambarArtikel(self):
        return self.gambar
        
        