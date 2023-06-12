from models.db import mysql


class TanamanModels:
    def __init__(self, id_tanaman, nama_tanaman, tanggal_tanaman, deskripsi_tanaman, gambar):
        self.id_tanaman = id_tanaman
        self.nama_tanaman = nama_tanaman
        self.tanggal_tanaman = tanggal_tanaman
        self.deskripsi_tanaman = deskripsi_tanaman
        self.gambar = gambar
        
        cursor = mysql.connection.cursor()
        query = '''
            INSERT INTO tanaman
            (id_tanaman, nama_tanaman, tanggal_tanaman, deskripsi_tanaman, gambar)
            VALUES (NULL, %s, NOW(), %s, %s)
        '''
        values = (self.nama_tanaman, self.deskripsi_tanaman, self.gambar)
        cursor.execute(query, values)

        mysql.connection.commit()
        cursor.close()

    @classmethod
    def getAllTanaman(cls):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM tanaman")

        dataTanaman = cursor.fetchall()

        # If empty set
        if len(dataTanaman) == 0:
            cursor.close()
            return None
        else:
            listTanaman = []
            for data in dataTanaman:
                id_tanaman, nama_tanaman, tanggal_tanaman, deskripsi_tanaman, gambar = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tanaman = id_tanaman
                self.nama_tanaman = nama_tanaman
                self.tanggal_tanaman = tanggal_tanaman
                self.deskripsi_tanaman = deskripsi_tanaman
                self.gambar = gambar

                listTanaman.append(self)

            cursor.close()
            return listTanaman

    @classmethod
    def getTanaman(cls, idTanaman):
        cursor = mysql.connection.cursor()

        query = '''
            SELECT * 
            FROM tanaman
            WHERE id_tanaman = %s
        '''
        cursor.execute(query, (idTanaman,))
        dataTanaman = cursor.fetchall()

        # If empty set
        if len(dataTanaman) == 0:
            cursor.close()
            return None
        else:
            listTanaman = []
            for data in dataTanaman:
                id_tanaman, nama_tanaman, tanggal_tanaman, deskripsi_tanaman, gambar = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tanaman = id_tanaman
                self.nama_tanaman = nama_tanaman
                self.tanggal_tanaman = tanggal_tanaman
                self.deskripsi_tanaman = deskripsi_tanaman
                self.gambar = gambar

                listTanaman.append(self)

            cursor.close()
            return listTanaman
    
    @classmethod
    def deleteTanaman(cls, idTanaman):
        try:
            cursor = mysql.connection.cursor()
            query = '''
                DELETE FROM jurnal
                WHERE id_tanaman = %s
            '''
            cursor.execute(query, (idTanaman,))
            query = '''
                DELETE FROM todolist
                WHERE id_tanaman = %s
            '''
            cursor.execute(query, (idTanaman,))
            query = '''
                DELETE FROM tanaman
                WHERE id_tanaman = %s
            '''
            cursor.execute(query, (idTanaman,))
            
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", str(e))
            mysql.connection.rollback()
            
    @classmethod
    def editTanaman(cls, idTanaman, nama_tanaman, deskripsi_tanaman, gambar):
        try:
            cursor = mysql.connection.cursor()
            query = '''
                UPDATE tanaman
                SET nama_tanaman = %s,
                    deskripsi_tanaman = %s,
                    gambar = %s
                WHERE id_tanaman = %s
            '''
            values = (nama_tanaman, deskripsi_tanaman, gambar, idTanaman)
            cursor.execute(query, values)
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", str(e))
            mysql.connection.rollback()
        

    def getIDTanaman(self):
        return self.id_tanaman

    def getNamaTanaman(self):
        return self.nama_tanaman

    def getTanggalTanaman(self):
        return self.tanggal_tanaman

    def getDeskripsiTanaman(self):
        return self.deskripsi_tanaman

    def getGambarTanaman(self):
        return self.gambar