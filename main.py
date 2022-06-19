import sys
import data_access

sql = ""

if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit(0)
    db_file = sys.argv[1]
    conn = data_access.get_connection(db_file)
    # data_access.execute_sql(conn, sql)
