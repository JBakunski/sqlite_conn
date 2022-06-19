import sys
import data_access
import presentation

# Add data to database
project_1 = (1, "Powtórka z angielskiego", "2020-05-11", "2021-06-10",)
project_2 = (2, "Powtórka z matematyki", "2022-01-31", "2022-06-30",)
task = (1, 1, "Czasowniki regularne", "Zapamiętaj czasowniki ze strony 20", "Zakończone", "2020-05-11", "2020-05-12",)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit(0)
    db_file = sys.argv[1]
    data_access.create_database(db_file)
    connection = data_access.get_connection(db_file)
    data_access.add_project(connection, project_1)
    data_access.add_project(connection, project_2)
    data_access.add_task(connection, task)
    presentation.display_all_items(data_access.read_all(connection, 'projects'))
    presentation.display_selected_item(data_access.read_item_by_id(connection, 'tasks', 1))
    presentation.display_all_items(data_access.read_where(connection, 'projects', name="Powtórka z matematyki"))
    data_access.update(connection, 'projects', 2, start_date="2023-01-31", end_date='2023-12-31')
    data_access.delete_all(connection, 'tasks')
    data_access.delete_where(connection, 'projects', id=2)

    