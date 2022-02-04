from flask_restful import Resource
from flask import request
from models.user import UserModel
from schemas.user import UserSchema
from app.messages import (
    USER_NOT_FOUND,
    USER_ALREADY_EXISTS,
    ERROR_GETTING_USER,
    ERROR_INSERTING_USER,
    USER_CREATED_SUCCESSFULLY,
)

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class User(Resource):
    @classmethod
    def get(cls, name):
        try:
            user = UserModel.find_by_name(name)
        except:
            return {"message": ERROR_GETTING_USER}, 500

        if user:
            return user_schema.dump(user)
        return {"message": USER_NOT_FOUND}, 404

    @classmethod
    def post(cls, name):
        try:
            user = UserModel.find_by_name(name)
        except:
            return {"message": ERROR_GETTING_USER}, 500

        if user:
            return {"message": USER_ALREADY_EXISTS}, 400

        user_json = request.get_json()
        user_json["name"] = name

        user = user_schema.load(user_json)

        try:
            user.save_to_db()
        except:
            return {"message": ERROR_INSERTING_USER}, 500

        return {"message": USER_CREATED_SUCCESSFULLY}, 201


class UserList(Resource):
    @classmethod
    def get(cls):
        return {"users": user_list_schema.dump(UserModel.find_all())}, 200
