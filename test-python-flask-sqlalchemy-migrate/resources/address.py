from flask_restful import Resource
from flask import request
from models.address import AddressModel
from models.user import UserModel
from schemas.address import AddressSchema
from app.messages import USER_NOT_FOUND, ERROR_INSERTING_ADDRESS

address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)


class Address(Resource):
    @classmethod
    def post(cls, user_id: int):

        if UserModel.query.get(user_id):
            address_json = request.get_json()
            address_json["user_id"] = user_id
            address = address_schema.load(address_json)
        else:
            return {"message": USER_NOT_FOUND}, 400

        try:
            address.save_to_db()
        except:
            return {"message": ERROR_INSERTING_ADDRESS}, 500

        return address_schema.dump(address), 201


class AddressList(Resource):
    @classmethod
    def get(cls):
        return {"addresses": address_list_schema.dump(AddressModel.find_all())}, 200
