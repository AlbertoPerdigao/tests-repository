from flask_restful import Resource, reqparse
from models.address import AddressModel

class Address(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', 
        type=str, 
        required=True,
        help="This field cannot be left blank!"
    )

    def post(cls, user_id):
        data = Address.parser.parse_args()        
        address = AddressModel(email=data['email'], user_id=user_id)

        try:
            address.save_to_db()
        except:
            return {"message": "An error occurred inserting the address."}, 500
    
        return address.json(), 201


class AddressList(Resource):
    def get(self):
        addresses = [address.json() for address in AddressModel.find_all()]        
        return {'addresses': addresses}, 200