from flask_sqlalchemy import Model
from sqlalchemy import true
from app import db
import datetime
# from .user_cv import UserPublic
from sqlalchemy.orm import backref




class Careers(db.Model):
    # con
    

    id = db.Column(db.Integer,primary_key=True)
    careers_name = db.Column(db.String(255),unique=True, nullable=False)
    describe = db.Column(db.String(1000))
    frofession_id = db.Column(db.Integer, db.ForeignKey("frofession.id"))
    # frofession = db.relationship("Frofession", backref=backref("frofession", uselist=False))

    def __init__(self,careers_name,describe,frofession_id) -> None:
        self.careers_name = careers_name
        self.describe = describe
        self.frofession_id = frofession_id
    def obj_person(self):
        obj = dict(id = self.id,careers_name=self.careers_name,describe=self.describe,frofession_id=self.frofession_id)
        return obj




# Nghe nghiep
class Frofession(db.Model):
    # cha 

    id  = db.Column(db.Integer,primary_key=True)
    frofession_name = db.Column(db.String(255),unique=True, nullable=False)
    describe = db.Column(db.String(1000))
    career = db.relationship('Careers', backref='frofession')

    def __init__(self,frofession_name , describe) -> None:
        self.frofession_name = frofession_name
        self.describe = describe
    def obj_person(self):
        obj = dict(id = self.id,frofession_name=self.frofession_name,describe=self.describe)
        return obj
    

        




# 1 - Frofession   -> n Careers