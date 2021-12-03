import sqlite3
from sqlite3.dbapi2 import Cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


def create_table():
    create_table = '''CREATE TABLE IF NOT EXISTS users(
        id INT,
        username TEXT,
        password TEXT
    );
    '''

    cursor.execute(create_table)


def add_user(user):
    insert_query = 'INSERT INTO users VALUES (?, ?, ?);'
    cursor.execute(insert_query, user)

    connection.commit()


def add_users(users):
    insert_query = 'INSERT INTO users VALUES (?, ?, ?);'
    cursor.executemany(insert_query, users)

    connection.commit()


def main():
    create_table()

    # user = (1, 'gabs', '1234')
    # add_user(user)

    # users = [
    #     (1, 'admin', 'admin'),
    #     (2, 'gabs', '1234'),
    #     (3, 'lari', '1234'),
    # ]
    # add_users(users)

    select_query = 'SELECT * FROM users'

    for row in cursor.execute(select_query):
        print(row)

    connection.close()


if __name__ == '__main__':
    main()
