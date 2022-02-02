from email.headerregistry import Address
from app import api
from resources.user import User, UserList
from resources.address import Address, AddressList

api.add_resource(UserList, '/users')
api.add_resource(User, '/user/<string:name>')
api.add_resource(Address, '/address/<int:user_id>')
api.add_resource(AddressList, '/addresses')