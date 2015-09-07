"""
Controller
"""

from sqlalchemy import create_engine, sql

class DB_Connection:
    def __init__(self):
        from instance.config import PG_USER, PG_PASSWORD
        db_uri = "postgresql://" + PG_USER + ":" + PG_PASSWORD + "@localhost/shrecdb"
        self.engine = create_engine(db_uri)

    def make_connection(self):
        self.connection = self.engine.connect()
        return self.connection

    def close_connection(self, connection):
        return connection.close()

""" test
query_books = "SELECT * FROM books"
DB = DB_Connection()
books_con = DB_Connection.make_connection(DB)
books = books_con.execute(sql.text(query_books))
DB_Connection.close_connection(DB, books_con)
"""

