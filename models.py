from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, password):
        self.name = name
        self.password = result_all

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Test(db.Model):
    __tablename__ = 'tests'
    
    id = db.Column(db.String(), primary_key=True)
    text = db.Column(db.String())

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.String(), primary_key=True)
    speed = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    mistakes = db.Column(JSON)

    def __init__(self, speed, accuracy, mistakes):
        self.speed = speed
        self.accuracy = accuracy
        self.mistakes = mistakes

    def __repr__(self):
        return '<id {}>'.format(self.id)

