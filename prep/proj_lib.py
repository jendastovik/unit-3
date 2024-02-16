import sqlite3

class DatabaseWorker:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
    def run_query(self, query:str):
        self.cursor.execute(query)
        self.conn.commit()

    def insert(self, username, password, email):
        query = f"""INSERT INTO users (email, password, username) VALUES ('{username}', '{password}', '{email}')"""
        self.run_query(query)
    
    def search(self, for_what = "*", where = "",multiple=False):
        query = f"SELECT {for_what} FROM users {where}"
        result = self.cursor.execute(query)
        if multiple:
            return result.fetchall() # returns multiple valuses in a list
        else:
            return result.fetchone() # returns a singele value
    
    def create(self):
        query = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL UNIQUE,
            password VARCHAR(256) NOT NULL,
            username TEXT NOT NULL
            )"""
        self.run_query(query)

    def close(self):
        self.conn.close()