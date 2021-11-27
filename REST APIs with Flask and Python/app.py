from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x.get('name') == name, items), None)

        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x.get('name') == name, items), None):
            return {'message', 'This name already be used'}, 400

        req = request.get_json()

        item = {'name': name, 'price': req.get('price')}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return items, 201


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run()
