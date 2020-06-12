import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (x_coordinates TEXT, y_coordinates TEXT);")
    

def add_entry(entry_x_coordinates, entry_y_coordinates):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_x_coordinates, entry_y_coordinates)
        )

def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor

