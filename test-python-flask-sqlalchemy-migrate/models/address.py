from typing import List
from sqlalchemy.sql import func
from app import db


class AddressModel(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # user = db.relationship("UserModel")

    def __repr__(self) -> str:
        return self.email

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls) -> List["AddressModel"]:
        return cls.query.all()
