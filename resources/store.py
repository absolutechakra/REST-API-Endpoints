from flask_restful import Resource
# from flask_restplus import Resource
from models.store import StoreModel


class Store(Resource):
    
    def get(self, name):
        """
        Get a store by name
        :param str name:     Store name
        :return:
        """
        store = StoreModel.find_by_name(name=name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    def post(self, name):
        """
        Create an store by name
        :param str name:     Store name
        :return:
        """
        if StoreModel.find_by_name(name=name):
            return {'message': 'Store already exists!'}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error while creating a store.'}, 500
        return store.json(), 201
    
    def delete(self, name):
        """
        Delete an store by name
        :param str name:     Item name
        :return:
        """
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted!'}
    
class StoreList(Resource):
    
    def get(self):
        """
        Get the list of stores
        :return:
        """
        return {'stores': [store.json() for store in StoreModel.query.all()]}