import sqlite3

class DBManager():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open_db(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def get_categories(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM category''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def create_article(self, title, description, text, author_id, category_id):
        self.open_db()
        self.cursor.execute('''INSERT INTO article (title, author_id, text, category_id, description) 
                            VALUES (?, ?, ?, ?, ?)''', (title, author_id, text, category_id, description))
        self.conn.commit()
        self.conn.close()

    def get_article(self, article_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM article WHERE id=?''', (article_id,))
        data = self.cursor.fetchone()
        self.conn.close()
        return data