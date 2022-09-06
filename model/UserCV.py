import email
from flask_sqlalchemy import Model
from sqlalchemy import true
from app import db


# flask db init 
# flask db migrate -m "init db"
# flask db upgrade

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True, nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    passwd = db.Column(db.String(255),unique=True, nullable=False)
    def __init__(self,email,username,passwd,) -> None:
        self.email = email
        self.username = username
        self.passwd = passwd
    def obj_person(self):
        obj = dict(id = self.id,email=self.email,username = self.username ,passwd = self.passwd)
        return obj
