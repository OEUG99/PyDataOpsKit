import mysql.connector
from mysql.connector import Error

from PyDataOpsKit import AbstractDatabaseStrategy


class MySQLStrategy(AbstractDatabaseStrategy):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None

        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )

            if self.conn.is_connected():
                self.cursor = self.conn.cursor()

                # Check if the database exists
                self.cursor.execute(f"SHOW DATABASES LIKE '{self.database}'")
                result = self.cursor.fetchone()

                # Create the database if it doesn't exist.
                if not result:
                    self.cursor.execute(f"CREATE DATABASE {self.database}")
                    print(f"Database '{self.database}' created successfully.")

                # Select the database
                self.cursor.execute(f"USE {self.database}")
                print(f"Database '{self.database}' selected successfully.")
            else:
                raise Exception("Unable to connect to the database server.")

        except Error as e:
            print("Error while connecting to MySQL:", e)

    def close(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("MySQL connection is closed.")

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
