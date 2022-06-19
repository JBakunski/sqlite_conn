import sys
import data_access




if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit(0)
    db_file = sys.argv[1]
    data_access.create_database(db_file)
