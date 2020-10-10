from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    name = db.Column(db.String())
    id = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, name, password):
        self.name = name
        self.password = result_all

    def __repr__(self):
        return '<id {}>'.format(self.id)
