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

        new_store = {
            'name': data['name']
        }

        stores.append(new_store)
        response = make_response(new_store, 201)

        return response
        

    
api.add_resource(Home, '/')
api.add_resource(Store, '/stores')

if __name__ == '__main__':
    app.run(port=5555, debug=True)