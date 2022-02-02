from app import db

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    cpf = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(20))
    addresses = db.relationship('AddressModel', backref='user', lazy='dynamic')    
    
    def __init__(self, name, cpf, password):        
        self.name = name
        self.cpf = cpf
        self.password = password
        self.addresses = []

    def __repr__(self) -> str:
        return '<User {}>'.format(self.name, self.cpf)

    def json(self):
        adresses = [address.email for address in self.addresses.all()]
        return {'id': self.id, 'name': self.name, 'cpf': self.cpf, 'password': self.password, 'addresses': adresses }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 

    @classmethod
    def find_all(cls):
        return cls.query.all();

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from users where name = name limit 1   