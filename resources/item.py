from models.item import ItemModel
from flask_restful import Resource, reqparse
# from flask_restplus import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank!')
    parser.add_argument('price', type=float, required=True, help='Price cannot be blank!')
    parser.add_argument('store_id', type=int, required=True, help='Every item need a store id!')
    
    @jwt_required()
    def get(self, name):
        """
        Get the item by name
        :param str name:     Item name
        :return:
        """
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
    
    def post(self, name):
        """
        Create a item by name
        :param str name:     Item name
        :return:
        """
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name %s already exists' % name}, 400
        
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting an item.'}, 500
        
        return item.json(), 201
    
    def delete(self, name):
        """
        Delete an item by name
        :param str name:     Item name
        :return:
        """
        item = ItemModel.find_by_name(name=name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted!'}
    
    def put(self, name):
        """
        Update the item by its name
        :param str name:     Item name
        :return:
        """
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            
        item.save_to_db()
        return item.json()


class Items(Resource):
    
    def get(self):
        """
        Get the list of items
        :return:            List of items
        """
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
