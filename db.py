import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db.sql')
        self.create_db()
        
    def create_db(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def save_to_db(self,name,email,message):
        c = self.conn.cursor()
        c.execute("INSERT INTO users (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        self.conn.commit()