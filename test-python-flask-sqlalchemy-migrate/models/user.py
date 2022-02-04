from typing import List
from app import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    addresses = db.relationship("AddressModel", backref="user", lazy="dynamic")

    def __repr__(self) -> str:
        return "<User {}>".format(self.name, self.cpf)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> "UserModel":
        return cls.query.filter_by(
            name=name
        ).first()  # select * from users where name = name limit 1

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()