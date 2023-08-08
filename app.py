from flask import Flask, make_response, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]

class Home(Resource):
    def get(self):
        return 'This is the home page :)'

class Store(Resource):
    def get(self):
        response = make_response(stores, 200)

        return response
    
    def post(self):
        data = request.get_json()

        new_store = {'name': data['name'], 'items': []}

        stores.append(new_store)
        response = make_response(new_store, 201)

        return response
    
class StoreByName(Resource):
    def get(self, name):
        for s in stores:
            if s['name'] == name:
                print(name)
                response = make_response(s, 201)

                return response
        response = make_response({'error': '404, Store not found'}, 404)
        
        return response
    
class StoreItem(Resource):
    def get(self, name):
        pass

    def post(self, name):
        data = request.get_json()

        for s in stores:
            if s['name'] == name:
                new_item = {'name': data['name'], 'price': data['price']}
                s['items'].append(new_item)

                response = make_response(new_item, 201)
                return response
            
        response = make_response({'error': '404, Store not found'}, 404)
        return response
    
api.add_resource(Home, '/')
api.add_resource(Store, '/store')
api.add_resource(StoreByName, '/store/<string:name>')
api.add_resource(StoreItem, '/store/<string:name>/item')

if __name__ == '__main__':
    app.run(port=5555, debug=True)