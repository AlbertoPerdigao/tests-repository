from app import ma
from models.user import UserModel
from schemas.address import AddressSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    addresses = ma.Nested(AddressSchema, many=True)

    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
        load_instance = True
