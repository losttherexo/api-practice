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
        id = uuid.uuid4().hex

        new_store = {**data, "id": id}

        stores[id] = new_store
        response = make_response(new_store, 201)

        return response
    
class StoreByName(Resource):
    def get(self, store_id):
        try:
            response = make_response(stores['store_id'], 200)

            return response
        except KeyError: 
            abort(404, message="Store not found.")
    
class Item(Resource):
    def get(self):
        response = make_response(list(items.values()), 200)

        return response

    def post(self):
        data = request.get_json()

        if data['store_id'] not in stores:
            abort(404, message="Store not found.")

        id = uuid.uuid4().hex
        item = {**data, 'id': id}
        response = make_response(item, 201)

        return response
    
class ItemByName(Resource):
    def get(self, item_id):
        try:
            response = make_response(items['item_id'], 200)

            return response
        except KeyError: 
            abort(404, message="Item not found.")

api.add_resource(Home, '/')
api.add_resource(Store, '/store')
api.add_resource(StoreByName, '/store/<string:store_id>')
api.add_resource(Item, '/item')
api.add_resource(ItemByName, '/item/<string:item_id>')

if __name__ == '__main__':
    app.run()