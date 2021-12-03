import sqlite3

DB_NAME = 'data.db'


def main():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Users table
    create_users_table = '''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    );
    '''
    cursor.execute(create_users_table)
    cursor.execute('INSERT INTO users VALUES (NULL, "admin", "admin");')

    # Items table
    create_items_table = '''CREATE TABLE IF NOT EXISTS items (
        name TEXT,
        price REAL
    );
    '''
    cursor.execute(create_items_table)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
