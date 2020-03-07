from flask import Flask
from flask_restful import Api
# from flask_restplus import Api
from flask_jwt import JWT
from db import db
from config import Config
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList
from security import authenticate, idenity


app = Flask(__name__)
app.secret_key = 'Hitesh'
app.config.from_object(Config)
api = Api(app)
# api = Api(app, version='1.0', doc='/swagger', title='REST API Endpoints', description='Flask REST API Endpoints')
# api.add_namespace(item)


@app.before_first_request
def create_tables():
    db.create_all()
    
    
jwt = JWT(app, authenticate, idenity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')

