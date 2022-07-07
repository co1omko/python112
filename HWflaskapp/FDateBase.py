import sqlite3


class FDateBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_kurs(self, title, price, text):
        try:
            self.__cur.execute("INSERT INTO kurs VALUES(NULL, ?, ?, ?)", (title, price, text))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добаления курс в БД" + str(e))
            return False
        return True

    def get_kurs(self, kurs_id):
        try:
            self.__cur.execute(f"SELECT title, price, text FROM kurs WHERE id = {kurs_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))

        return False, False, False

    def get_kurs_annonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text, price FROM kurs")
            res = self.__cur.fetchall
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))

        return []