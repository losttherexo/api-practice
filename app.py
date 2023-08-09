import uuid
from flask import Flask, make_response, request
from flask_smorest import abort
from flask_restful import Resource, Api
from db import items, stores

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'This is the home page :)'

class Store(Resource):
    def get(self):
        response = make_response(list(stores.values()), 200)

        return response
    
    def post(self):
        data = request.get_json()

        if 'name' not in data:
            abort(400, message='Incorrect JSON Payload.')

        for store in stores.values():
            if data['name'] == store['name']:
                abort(400, message='Store already exists.')

        id = uuid.uuid4().hex

        new_store = {**data, 'id': id}

        stores[id] = new_store
        response = make_response(new_store, 201)

        return response
    
class StoreById(Resource):
    def get(self, store_id):
        try:
            response = make_response(stores[store_id], 200)

            return response
        except KeyError: 
            abort(404, message='Store not found.')
    
class Item(Resource):
    def get(self):
        response = make_response(list(items.values()), 200)

        return response

    def post(self):
        data = request.get_json()

        if ('price' not in data
            or 'name' not in data or 'store_id' not in data):
            abort(400, message='Incorrect JSON payload.')

        for item in items.values():
            if (
                data['name'] == item['name']
                and data['store_id'] == item['store_id']
            ):
                abort(400, message='Item already exists.')

        if data['store_id'] not in stores:
            abort(404, message='Store not found.')

        id = uuid.uuid4().hex
        item = {**data, 'id': id}
        items[id] = item
        response = make_response(item, 201)

        return response
    
class ItemById(Resource):
    def get(self, item_id):
        try:
            response = make_response(items[item_id], 200)

            return response
        except KeyError: 
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            response = make_response({'message': 'Item Deleted.'}, 204)

            return response
        except KeyError:
            abort(404, message="Item not found.")

api.add_resource(Home, '/')
api.add_resource(Store, '/store')
api.add_resource(StoreById, '/store/<string:store_id>')
api.add_resource(Item, '/item')
api.add_resource(ItemById, '/item/<string:item_id>')

if __name__ == '__main__':
    app.run()