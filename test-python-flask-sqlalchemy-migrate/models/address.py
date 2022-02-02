from app import db
from datetime import datetime

class AddressModel(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.now())    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
    
    def __repr__(self):
        return self.email

    def json(self):
        user = {'id': self.user.id, 'name': self.user.name, 'cpf': self.user.cpf} # backref='user' in UserModel
        return {'id': self.id, 'email': self.email, 'created_at': self.created_at.isoformat(), 'user': user}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()    

    @classmethod
    def find_all(cls):
        return cls.query.all();