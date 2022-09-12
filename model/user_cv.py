from flask_sqlalchemy import Model
from sqlalchemy import true
from app import db


# flask db init 
# flask db migrate -m "init db"
# flask db upgrade

class UserPublic(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True, nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # personal_information_id = db.relationship("Child", back_populates="parent", uselist=False)
    def __init__(self,email,username,password) -> None:
        self.email = email
        self.username = username
        self.password = password
    def obj_person(self):
        obj = dict(id = self.id,email=self.email,username = self.username)
        return obj
