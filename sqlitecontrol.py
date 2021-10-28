import sqlite3

class Sqlitecontrol:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def get_name(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            try:
                return (result)[0][2]
            except:

                return None
    def exists(self, tg_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            try:
                return (result)[0][2]
            except:
                return None

    def add_name(self, tg_id, name="NOname"):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`tg_id`, `name`) VALUES(?,?)", (tg_id, name))

    def set_name(self, tg_id, name):
        with self.connection:
            self.cursor.execute("""UPDATE 'users' SET name = ? WHERE tg_id = ?""", (name, tg_id))



    def obr_set(self, tg_id, status):
        with self.connection:
            self.cursor.execute("""UPDATE 'users' SET obr = ? WHERE tg_id = ?""", (status, tg_id))

    def status_set(self, tg_id, status):
        with self.connection:
            self.cursor.execute("""UPDATE 'users' SET status = ? WHERE tg_id = ?""", (status, tg_id))

    def all_table(self):
        print(self.cursor.execute("""select * from sqlite_master
                    where type = 'table'""").fetchall())

    def obr_get(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            try:
                return (result)[0][3]
            except:

                return None

    def status_get(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            try:
                return (result)[0][5]
            except:

                return None

    def like_set(self, tg_id, n):
        with self.connection:
            self.cursor.execute("""UPDATE 'users' SET like = like + ? WHERE tg_id = ?""", (n, tg_id))

    def like_get(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            try:
                return (result)[0][4]
            except:

                return None

    def get_args(self, tg_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `tg_id` = ?", (tg_id,)).fetchall()
            try:
                return (str(result[0][6]).split(','))
            except:
                return None
    def set_args(self, tg_id, index, val):
        n = self.get_args(tg_id)
        n[index] = val
        with self.connection:
            self.cursor.execute("""UPDATE 'users' SET args = ? WHERE tg_id = ?""", ('{0},{1},{2},{3}'.format(n[0],n[1],n[2],n[3]), tg_id))
    def null_args(self, tg_id):
        with self.connection:
            self.cursor.execute("""UPDATE 'users' SET args = ? WHERE tg_id = ?""", ('0,0,0,0', tg_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
    def printf (self):
        t = ''
        self.cursor.execute("SELECT * FROM `users`")
        rows = self.cursor.fetchall()

        for row in rows:
            t += ('\n' + str(row))
        return (t)
if __name__ == '__main__':
    new = Sqlitecontrol('TGBase.db')
    new.add_name("123", " kjk")
    print(new.get_name("123"))
