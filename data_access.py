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
    create_orders_table_sql = """
    CREATE TABLE IF NOT EXISTS orders
    (
        id int NOT NULL,
        order_number varchar(255) NOT NULL,
        order_date text,
        delivery_date text,
        PRIMARY KEY(id)
    );
    """
    create_orderlines_table_sql = """
    CREATE TABLE IF NOT EXISTS orderlines
    (
        id int NOT NULL,
        order_id int NOT NULL,
        product_number varchar(255) NOT NULL,
        description varchar(255),
        qty int NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(order_id) REFERENCES orders(id)
    );
    """
    conn = get_connection(db_file)
    if conn:
        execute_sql(conn, create_orders_table_sql)
        execute_sql(conn, create_orderlines_table_sql)
    
def add_order(conn, order):
    sql = """
    INSERT INTO orders (id, order_number, order_date, delivery_date) VALUES (?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()
    print("New order added")

def add_orderline(conn, orderline):
    sql = """INSERT INTO orderlines (id, order_id, product_number, description, qty) VALUES (?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, orderline)
    conn.commit()
    print("New orderline added")

def read_all(conn, table):
    sql = f"""SELECT * FROM {table}"""
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def read_item_by_id(conn, table, id):
    sql = f"SELECT * FROM {table} WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (id, ))
    row = cur.fetchone()
    return row

def read_where(conn, table, **condition):
    cur = conn.cursor()
    cond = []
    values = ()
    for k, v in condition.items():
        cond.append(f"{k}=?")
        values +=(v, )
    c = " AND ".join(cond)
    cur.execute(f"SELECT * FROM {table} WHERE {c}", values)
    rows = cur.fetchall()
    return rows

def update(conn, table, id, **kwargs):
    parameters = [f"{k}=?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )
    try:
        cur = conn.cursor()
        cur.execute(f"UPDATE {table} SET {parameters} WHERE id =?", values)
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)

def delete_all(conn, table):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table}")
    conn.commit()
    print("Data deleted")

def delete_where(conn, table, **condition):
    cur = conn.cursor()
    cond = []
    values = ()
    for k, v in condition.items():
        cond.append(f"{k}=?")
        values += (v, )
    c = " AND ".join(cond)
    cur.execute(f"DELETE FROM {table} WHERE {c}", values)
    conn.commit()
