import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')

    def load_data(self):
        request = "SELECT question, answer FROM quiz"
        info = self.conn.execute(request).fetchall()
        data = []
        for i in range(len(info)):
            data.append({'id': i, 'question': info[i][0], 'answer': info[i][1], 'user_answer': '', 'is_showed': 0})

        return data

#
# db = DB()
# db.load_data()
