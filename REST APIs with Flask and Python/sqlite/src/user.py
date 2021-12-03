from flask_restful import Resource, reqparse
import sqlite3


class User:
    def __init__(self, _id, username, password) -> None:
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE id = ?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        user = cls(*row) if row else None

        connection.close()
        return user

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username = ?'
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        user = cls(*row) if row else None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='Username is mandatory'
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='Password is mandatory'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data.get('username')):
            return {'message': 'Username alread exists'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL, ?, ?);'
        cursor.execute(query, (data.get('username'), data.get('password')))

        connection.commit()
        connection.close()

        return {'message': 'User created successfully!'}, 201
