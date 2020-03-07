from models.user import UserModel
from flask_restful import Resource, reqparse
# from flask_restplus import Resource, reqparse


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Username cannot be blank!')
    parser.add_argument('password', type=str, required=True, help='Password cannot be blank!')
    
    def post(self):
        """
        Register a User
        :return:
        """
        data = self.parser.parse_args()
        if UserModel.find_by_username(data.get('username')):
            return {'message': 'A user with username already exists'}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {'message': 'User created successfully!'}, 201