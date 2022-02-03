from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cpf', 
        type=str, 
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password', 
        type=str, 
        required=True,
        help="Every user needs a password."
    ) 

    @classmethod
    def get(cls, name):
        try:
            user = UserModel.find_by_name(name)
        except:
            return {'message': 'An error occurred getting the user.'}, 500

        if user:
            return user.json()
        return {'message': 'User not found'}, 404
    
    @classmethod
    def post(cls, name):        
        if UserModel.find_by_name(name):
            return {'message': "An user with name '{}' already exists.".format(name)}, 400

        data = User.parser.parse_args()
        user = UserModel(name, data['cpf'], data['password']) # UserModel(name, **data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500
    
        return user.json(), 201


class UserList(Resource):
    @classmethod
    def get(cls):
        users = [user.json() for user in UserModel.find_all()]        
        return {'users': users}, 200
        