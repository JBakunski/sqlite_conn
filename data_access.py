import sqlite3
from sqlite3 import Error


def get_connection(db_file):
    with sqlite3.Connection(db_file) as conn:
        print(f"Connected to {db_file}")
        return conn


def execute_sql(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
    except Error as e:
        print(e)