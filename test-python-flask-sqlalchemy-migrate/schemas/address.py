from app import ma
from models.address import AddressModel


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AddressModel
        load_only = ("user",)
        dump_only = ("id",)
        load_instance = True
        include_fk = True
