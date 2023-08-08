from flask import Flask
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
        return "This is the home page :)"

class Store(Resource):
    def get(self):
        return {"stores": stores}, 200
    
api.add_resource(Home, '/')
api.add_resource(Store, '/stores')

if __name__ == '__main__':
    app.run(debug=True)