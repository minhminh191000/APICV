from tokenize import Name
from unicodedata import name
from flask_sqlalchemy import Model
from sqlalchemy import true
from app import db
from sqlalchemy.orm import backref

# flask db init 
# flask db migrate -m "init db"
# flask db upgrade


# thong tin profile
class JobRegistration(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    user_id  = db.Column(db.Integer,db.ForeignKey("user_public.id"))
    userpublic = db.relationship("UserPublic", backref=backref("jobregistration", uselist=False))
    job_id = db.Column(db.Integer)



    def __init__(self,user_id,job_id) -> None:
        self.user_id = user_id
        self.job_id = job_id
    def obj_person(self):
        obj = dict(id = self.id,user_id=self.user_id,job_id = self.job_id)
        return obj

        
class SaveJob(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    user_id  = db.Column(db.Integer,db.ForeignKey("user_public.id"))
    userpublic = db.relationship("UserPublic", backref=backref("savejob", uselist=False))
    job_id = db.Column(db.Integer)



    def __init__(self,user_id,job_id) -> None:
        self.user_id = user_id
        self.job_id = job_id
    def obj_person(self):
        obj = dict(id = self.id,user_id=self.user_id,job_id = self.job_id)
        return obj



    

