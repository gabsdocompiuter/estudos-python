from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'gabsdocompiuter',
        'items': [
            {
                'name': 'development',
                'price': 80.00
            }
        ]
    }
]


@app.route('/store/')  # GET /store
def get_all_stores():
    return jsonify(stores)


@app.route('/store', methods=['POST'])  # POST /store
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')  # GET /store/<string:name>
def get_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify(store)

    return {'message': 'store not found'}


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }

    for store in stores:
        if store.get('name') == name:
            store.get('items').append(new_item)
            return jsonify(store)

    return {'message': 'store not found'}


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify(store.get('items'))


app.run()
