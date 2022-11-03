from flask_sqlalchemy import Model
from sqlalchemy import true
from app import db
import datetime
from .user_cv import UserPublic
from sqlalchemy.orm import backref


# thong tin ca nhan
class PersonalInformation(db.Model):


    id = db.Column(db.Integer,primary_key=True)
    fullname = db.Column(db.String(100))
    birth_of_day = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    userpublic_id = db.Column(db.Integer, db.ForeignKey("user_public.id"))
    userpublic = db.relationship("UserPublic", backref=backref("personalinformation", uselist=False))


    avatar_url = db.Column(db.String(255))
    position = db.Column(db.String(255))
    about = db.Column(db.String(255))
    skills = db.Column(db.String(255))
    resumeUrl = db.Column(db.String(255))


    information = db.relationship('Information', backref='personalinformation')

    def __init__(self,userpublic_id,fullname, birth_of_day, gender,phone,address,position,about,skills,avatar_url,resumeUrl) -> None:
        self.userpublic_id = userpublic_id
        self.fullname = fullname
        self.birth_of_day = birth_of_day
        self.gender = gender
        self.phone = phone
        self.address = address
        self.position = position
        self.about = about
        self.skills = skills
        self.avatar_url = avatar_url
        self.resumeUrl = resumeUrl
        
        # position=data.get("position"),about=data.get("about"),skills=data.get("skills"),avatar_url=data.get("avatar_url")
        # position = self.position,about = self.about,skills = self.skills,avatar_url = self.avatar_url
        # self.address = address

    def obj_person(self):
        obj = dict(id = self.id,fullname=self.fullname,birth_of_day = self.birth_of_day,gender = self.gender,phone = self.phone,address = self.address,position = self.position,about = self.about,skills = self.skills,avatar_url = self.avatar_url,resumeUrl = self.resumeUrl)
        return obj


# Thong Tin CV
class Information(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    title_1 = db.Column(db.String(255))
    title_2 = db.Column(db.String(255))
    date_in = db.Column(db.String(255))
    date_out = db.Column(db.String(255))
    description_details = db.Column(db.String(1000))
    personalinformation_id = db.Column(db.Integer, db.ForeignKey("personal_information.id"))

    def __init__(self,name,title_1,title_2,date_in,date_out,description_details,personalinformation_id) -> None:
        self.name = name
        self.title_1 = title_1
        self.title_2 = title_2
        self.date_in = date_in
        self.date_out = date_out
        self.description_details = description_details
        self.personalinformation_id = personalinformation_id
    def obj_person(self):
        obj  = dict(id=self.id ,name=self.name ,title_1=self.title_1,title_2=self.title_2,date_in=self.date_in,date_out=self.date_out,description_details=self.description_details,personalinformation_id=self.personalinformation_id)
        return obj
       
        
