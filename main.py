import sys
import data_access
import presentation

# Add data to database
project = (1, "Powtórka z angielskiego", "2020-05-11", "2021-06-10",)
task = (1, 1, "Czasowniki regularne", "Zapamiętaj czasowniki ze strony 20", "Zakończone", "2020-05-11", "2020-05-12",)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit(0)
    db_file = sys.argv[1]
    data_access.create_database(db_file)
    connection = data_access.get_connection(db_file)
    data_access.add_project(connection, project)
    data_access.add_task(connection, task)
    presentation.display_all_items(data_access.read_all(connection, 'projects'))
