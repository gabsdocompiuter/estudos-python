from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'maconha'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='Price is mandatory'
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x.get('name') == name, items), None)

        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x.get('name') == name, items), None):
            return {'message', 'This name already be used'}, 400

        req = Item.parser.parse_args()

        item = {'name': name, 'price': req.get('price')}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x.get('name') != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        req = Item.parser.parse_args()

        item = next(filter(lambda x: x.get('name') == name, items), None)

        if item is None:
            item = {'name': name, 'price': req.get('price')}
            items.append(item)
        else:
            item.update(req)

        return item


class ItemList(Resource):
    def get(self):
        return items, 201


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run()
