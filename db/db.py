import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to a sqlite database"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection("/home/jopuskar/PycharmProjects/Learning/db/my_db.db")