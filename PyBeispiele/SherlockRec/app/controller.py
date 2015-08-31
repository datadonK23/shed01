"""
Controller
"""

from sqlalchemy import create_engine

class DB_Connection:
    def __init__(self):
        from instance.config import PG_USER, PG_PASSWORD
        db_uri = "postgresql://" + PG_USER + ":" + PG_PASSWORD + "@localhost/shrecdb"
        engine = create_engine(db_uri)
        self.connection = self.make_connection(engine)
#FIXME
    def make_connection(self, engine):
        connection = engine.connect()
        return connection

    def close_connection(self):
        connection.close()

#query_books = "SELECT * FROM books"
#books_con = DB_Connection.make_connection()
#books = books_con.execute(sql.text(query_books))
#books_con.close_connection()