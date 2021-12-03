import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='price is mandatory'
    )

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)

        return item if item else {'message': 'item not fould'}

    @jwt_required()
    def post(self, name):
        if Item.find_by_name(name):
            return {'message': 'this name already be used'}, 400

        req = Item.parser.parse_args()

        item = {'name': name, 'price': req.get('price')}

        try:
            Item.create_item(item)

        except:
            return {'message': 'an error occurred inserting item'}, 500
        return item, 201

    @jwt_required()
    def delete(self, name):
        if Item.find_by_name(name) is None:
            return {'message': 'item not found'}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name, ))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        req = Item.parser.parse_args()

        old_item = Item.find_by_name(name)

        item = {'name': name, 'price': req.get('price')}

        if old_item:
            Item.update_item(item)
        else:
            Item.create_item(item)

        return item

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE name = ?;'

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {
                'name': row[0],
                'price': row[1]
            }

    @classmethod
    def create_item(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?);"

        cursor.execute(query, (item.get('name'), item.get('price')))

        connection.commit()
        connection.close()

    @classmethod
    def update_item(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price = ? WHERE name = ?;"

        cursor.execute(query, (item.get('price'), item.get('name')))

        connection.commit()
        connection.close()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items;'

        result = cursor.execute(query)
        items = []

        for row in result:
            items.append({
                'name': row[0],
                'price': row[1]
            })

        connection.close()

        if items:
            return items
        else:
            return {'message': 'No items found'}
