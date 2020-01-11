from flask import Flask
# from flask_restful import Api
from flask_restplus import Api
from flask_jwt import JWT
from webapp.db import db
from webapp.config import Config
from webapp.resources.user import UserRegister
from webapp.resources.item import Item, Items
from webapp.resources.store import Store, StoreList
from webapp.security import authenticate, idenity


app = Flask(__name__)
app.secret_key = 'Hitesh'
app.config.from_object(Config)
# api = Api(app)
api = Api(app, version='1.0', title='REST API Endpoints', description='Flask REST API Endpoints')
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
    app.run(debug=True)

