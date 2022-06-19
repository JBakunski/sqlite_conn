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

def create_database(db_file):
    create_projects_table_sql = """
    CREATE TABLE IF NOT EXISTS projects
    (
        id int NOT NULL,
        name varchar(255) NOT NULL,
        start_date text,
        end_date text,
        PRIMARY KEY(id)
    );
    """
    create_tasks_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks
    (
        id int NOT NULL,
        project_id int NOT NULL,
        name varchar(255) NOT NULL,
        description varchar(255),
        status varchar(100) NOT NULL,
        start_date text,
        end_date text,
        PRIMARY KEY(id),
        FOREIGN KEY(project_id) REFERENCES projects(id)
    );
    """
    conn = get_connection(db_file)
    if conn:
        execute_sql(conn, create_projects_table_sql)
        execute_sql(conn, create_tasks_table_sql)
    
def add_project(conn, project):
    sql = """
    INSERT INTO projects (id, name, start_date, end_date) VALUES (?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    print("New project added")

def add_task(conn, task):
    sql = """INSERT INTO tasks (id, project_id, name, description, status, start_date, end_date) VALUES (?,?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    print("New task added")


    
