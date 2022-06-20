import sys
import data_access
import presentation

# Add data to database
order_1 = (1, "ZA2022-1306", "2022-06-13", "2022-11-15")
order_2 = (2, "ZA2022-2205", "2022-05-22", "2022-09-10")
orderline_1 = (1, 1, "ESDS0ZZ144820", "Self drilling screw 4.8 x 20", 100000)
orderline_2 = (2, 1, "ESDS3ZZ144819", "Self drilling screw 4.8 x 19", 200000)
orderline_3 = (3, 2, "ESPS12PA1955285", "Sandwich panel screw 5.5 x 285", 30000)
orderline_4 = (4, 2, "ESDS15ZZ145535", "Self drilling screw 4.8 x 20", 100000)
orderline_5 = (5, 2, "ESPS6PA1955175", "Sandwich panel screw 5.5 x 175", 60000)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        exit(0)
    db_file = sys.argv[1]
    data_access.create_database(db_file)
    connection = data_access.get_connection(db_file)
    data_access.add_order(connection, order_1)
    data_access.add_order(connection, order_2)
    data_access.add_orderline(connection, orderline_1)
    data_access.add_orderline(connection, orderline_2)
    data_access.add_orderline(connection, orderline_3)
    data_access.add_orderline(connection, orderline_4)
    data_access.add_orderline(connection, orderline_5)
    presentation.display_all_items(data_access.read_all(connection, 'orders'))
    presentation.display_selected_item(data_access.read_item_by_id(connection, 'orderlines', 1))
    presentation.display_all_items(data_access.read_where(connection, 'orders', order_number="ZA2022-1306"))
    data_access.update(connection, 'orders', 2, delivery_date="2022-12-31")
    data_access.delete_all(connection, 'orderlines')
    data_access.delete_where(connection, 'orders', id=2)

    