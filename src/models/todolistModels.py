from models.db import mysql


class TodolistModels:
    def __init__(self, id_tdl, id_tanaman, waktu, deskripsi_tdl):
        self.id_tdl = id_tdl
        self.id_tanaman = id_tanaman
        self.waktu = waktu
        self.deskripsi_tdl = deskripsi_tdl
        
        cursor = mysql.connection.cursor()
        query = '''
            INSERT INTO todolist
            (id_tdl, id_tanaman, waktu, deskripsi_tdl)
            VALUES (NULL, %s, %s, %s)
        '''
        values = (self.id_tanaman, self.waktu, self.deskripsi_tdl)
        cursor.execute(query, values)

        mysql.connection.commit()
        cursor.close()

    @classmethod
    def getAllTodolist(cls):
        cursor = mysql.connection.cursor()
        cursor.execute('''
                       SELECT *
                       FROM todolist
                       ORDER BY waktu ASC
                       ''')

        dataTDL = cursor.fetchall()

        # If empty set
        if len(dataTDL) == 0:
            cursor.close()
            return None
        else:
            listTDL = []
            for data in dataTDL:
                id_tdl, id_tanaman, waktu, deskripsi_tdl = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tdl = id_tdl
                self.id_tanaman = id_tanaman
                self.waktu = waktu
                self.deskripsi_tdl = deskripsi_tdl

                listTDL.append(self)

            cursor.close()
            return listTDL

    @classmethod
    def getTodolistByIdTanaman(cls, idTanaman):
        cursor = mysql.connection.cursor()
        query = '''
            SELECT * 
            FROM todolist 
            WHERE id_tanaman = %s
            ORDER BY waktu ASC
        '''
        cursor.execute(query, (idTanaman,))
        dataTDL = cursor.fetchall()

        # If empty set
        if len(dataTDL) == 0:
            cursor.close()
            return None
        else:
            listTDL = []
            for data in dataTDL:
                id_tdl, id_tanaman, waktu, deskripsi_tdl = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tdl = id_tdl
                self.id_tanaman = id_tanaman
                self.waktu = waktu
                self.deskripsi_tdl = deskripsi_tdl

                listTDL.append(self)

            cursor.close()
            return listTDL
        
    @classmethod
    def getTodolistByIdTDL(cls, idTDL):
        cursor = mysql.connection.cursor()
        query = '''
            SELECT * 
            FROM todolist 
            WHERE id_tdl = %s
            ORDER BY waktu ASC
        '''
        cursor.execute(query, (idTDL,))
        dataTDL = cursor.fetchall()

        # If empty set
        if len(dataTDL) == 0:
            cursor.close()
            return None
        else:
            listTDL = []
            for data in dataTDL:
                id_tdl, id_tanaman, waktu, deskripsi_tdl = data

                # initialize class
                self = cls.__new__(cls)
                self.id_tdl = id_tdl
                self.id_tanaman = id_tanaman
                self.waktu = waktu
                self.deskripsi_tdl = deskripsi_tdl

                listTDL.append(self)

            cursor.close()
            return listTDL

    @classmethod
    def deleteTodolist(cls, idTDL):
        try:
            cursor = mysql.connection.cursor()
            query = '''
                DELETE FROM todolist
                WHERE id_tdl = %s
            '''
            cursor.execute(query, (idTDL,))
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", str(e))
            mysql.connection.rollback()
            
    @classmethod
    def editTodolist(cls, idTDL, waktu, deskripsi_tdl):
        try:
            cursor = mysql.connection.cursor()
            query = '''
                UPDATE todolist
                SET waktu = %s,
                    deskripsi_tdl = %s
                WHERE id_tdl = %s
            '''
            values = (waktu, deskripsi_tdl, idTDL)
            cursor.execute(query, values)
            mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print("Error:", str(e))
            mysql.connection.rollback()

    def getIDTDL(self):
        return self.id_tdl

    def getIDTanaman(self):
        return self.id_tanaman

    def getWaktuTDL(self):
        return self.waktu

    def getDeskripsiTDL(self):
        return self.deskripsi_tdl
