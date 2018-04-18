from sqlite3 import Error
import sys
from faker import Faker

from db import create_connection


def create_table(conn, create_table_sql):
    """create table from connection object i.e conn
    and create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("created!")
    except Error as e:
        print(e)


def insert(conn):
    if conn.cursor():
        c = conn.cursor()
        fake = Faker()
        for i in range(200):
            c.execute("INSERT INTO my_table (name, phone, bio, dob, gender, address,",
                      "longitude, latitude, img, social_link) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (fake.name(), fake.phone_number(), fake.sentence(), fake.date(), 'male', fake.address(),
                       '-158.355745', '-158.355745', fake.word(), fake.url()))
        print("Done 200!")
        conn.commit()


def create(conn):
    if conn.cursor():
        c = conn.cursor()
        c.execute("INSERT INTO my_table (name, phone, bio, dob, gender, address, longitude, latitude, img, social_link)"
                  "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6],
                                                           sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]))
        conn.commit()

def main():
    database = "/home/jopuskar/PycharmProjects/Learning/db/my_db.db"

    sql_create_my_table = """CREATE TABLE IF NOT EXISTS my_table (
                              id integer PRIMARY KEY,
                              name text NOT NULL,
                              phone text NOT NULL,
                              bio text NOT NULL,
                              dob text NOT NULL,
                              gender text NOT NULL,
                              address text NOT NULL,
                              longitude text NOT NULL,
                              latitude text NOT NULL,
                              img BLOB NOT NULL,
                              social_link text NOT NULL);"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_my_table)
        create(conn)
        print("Table Created!")
    else:
        print("Error! Cannot establish database connection!")


if __name__ == "__main__":
    main()