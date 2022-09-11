from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum

db= SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True )
    password = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    #todo = db.relationship('TODO', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.email}'


class STATUS(str,Enum):
   NotStarted = 'NotStarted'
   OnGoing = 'OnGoing'
   Completed = 'Completed'


class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String())
    description = db.Column(db.String())
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Enum(STATUS), default=STATUS.NotStarted)


    def __repr__(self) -> str:
        return 'Todo>>> {self.user_id}'
