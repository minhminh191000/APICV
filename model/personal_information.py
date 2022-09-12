from flask_sqlalchemy import Model
from sqlalchemy import true
from app import db
import datetime
from .user_cv import UserPublic
from sqlalchemy.orm import backref


class PersonalInformation(db.Model):


    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(100))
    birth_of_day = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    gender = db.Column(db.String(10))
    userpublic_id = db.Column(db.Integer, db.ForeignKey("user_public.id"))
    userpublic = db.relationship("UserPublic", backref=backref("personalinformation", uselist=False))

    def __init__(self,userpublic_id,fullname,birth_of_day,gender) -> None:
        self.userpublic_id = userpublic_id
        self.fullname = fullname
        self.birth_of_day = birth_of_day
        self.gender = gender
    def obj_person(self):
        obj = dict(id = self.id,fullname=self.fullname,birth_of_day = self.birth_of_day,gender = self.gender)
        return obj
        


