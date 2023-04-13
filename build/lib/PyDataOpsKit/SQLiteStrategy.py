import sqlite3
from sqlite3 import Error


class SQLiteStrategy:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"SQLite connection to '{self.db_file}' established successfully.")
        except Error as e:
            print("Error while connecting to SQLite:", e)

    def close(self):
        if self.conn:
            self.conn.close()
            print("SQLite connection is closed.")

    def query(self, query, params=None):
        if self.conn is None:
            self.connect()

        cur = self.conn.cursor()
        if params is not None:
            cur.execute(query, params)  # execute with params
        else:
            cur.execute(query)  # execute without params
        result = cur.fetchall()
        self.conn.commit()
        cur.close()
        return result
