from app import app ,db,get_current_user
from flask import jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity


from model.job_registration import JobRegistration as Job 
from model.job_registration import SaveJob as Sjob
from model.user_cv import *


import json
# from app import db,app
# from model.personal_information import *

class JobRegistration:


    @jwt_required()
    def get_data(self):
        user = get_current_user()
        # print("user ======",user.id)
        job_registration = db.session.query(Job).filter(Job.user_id == user.id).all()
        # print(job_registration)
        list_job = []
        for job in job_registration:
            name,company,salary,location = self.get_job(job.job_id)
            vals = {
                        "id":job.id,
                        "job_id":job.job_id,
                        "user_id":job.user_id,
                        "name":name,
                        "comapy":company,
                        "salary":salary,
                        "location":location
                    }
            list_job.append(vals)   

        
        
        return jsonify({"status":200,"data":list_job})


    @jwt_required()
    def create(self):
        if request.method == "POST":
            data = request.get_json()
            user_id = get_current_user().id
            job_id = data.get("job_id")
            job = Job(user_id=user_id,job_id=job_id)
            db.session.add(job)
            db.session.commit()
            return jsonify({"status":200,"message":"Create information"})

    @jwt_required()
    def delete(self):
        if request.method == "POST":
            data = request.get_json()
            job = db.session.query(Job).filter(Job.id == data.get("id")).first()
            if job is not None:
                db.session.delete(job)
                db.session.commit()
                return jsonify({"status":200,"message":"Delete information successfully"})
            return jsonify({"status":404,"message":"Delete information fail"})        

    






    def get_job(self,id):
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)
        for item in json_object:
            job_details =  item["job_details"]
            for i in job_details:
                salary = i["general_information"]["salary"]            
            if int(item["id"]) == int(id):
                return item["name"],item["company"],salary,i["location"]

class SaveJob:


    @jwt_required()
    def get_data(self):
        user = get_current_user()
        # print("user ======",user.id)
        job_registration = db.session.query(Sjob).filter(Sjob.user_id == user.id).all()
        print(job_registration)
        list_job = []
        for job in job_registration:
            name,company,salary,location = self.get_job(job.job_id)
            vals = {
                        "id":job.id,
                        "job_id":job.job_id,
                        "user_id":job.user_id,
                        "name":name,
                        "comapy":company,
                        "salary":salary,
                        "location":location
                    }
            list_job.append(vals)  

        
        
        return jsonify({"status":200,"data":list_job})


    @jwt_required()
    def create(self):
        if request.method == "POST":
            data = request.get_json()
            user_id = get_current_user().id
            job_id = data.get("job_id")
            job = Sjob(user_id=user_id,job_id=job_id)
            db.session.add(job)
            db.session.commit()
            return jsonify({"status":200,"message":"Create "})

    @jwt_required()
    def delete(self):
        if request.method == "POST":
            data = request.get_json()
            
            job = db.session.query(Sjob).filter(Sjob.id == data.get("id")).first()
            if job is not None:
                db.session.delete(job)
                db.session.commit()
                return jsonify({"status":200,"message":"Delete  successfully"})
            return jsonify({"status":404,"message":"Delete  fail"})

    @jwt_required()
    def check_save_job(self):
        if request.method == "POST":
            data = request.get_json()
            user = get_current_user().id
            print(type(user))
            print("day la user",user)
            save_job = db.session.query(Sjob).filter(Sjob.user_id == user).all()
            print("day la save_job",save_job)
            if save_job is not None:
                for i in save_job:
                    # print()
                    if i.job_id == data.get("job_id"):
                        return jsonify({"status":200,"message":True})
            return jsonify({"status":404,"message":False})   
    


    def get_job(self,id):
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)
        for item in json_object:
            job_details =  item["job_details"]
            for i in job_details:
                salary = i["general_information"]["salary"]            
            if int(item["id"]) == int(id):
                return item["name"],item["company"],salary,i["location"]
        

            





jobregistration = JobRegistration()
# # app.ad
app.add_enpoint("/jobinformation/create","create jobregistration",jobregistration.create,methods=["POST"])
app.add_enpoint("/jobinformation/get","get jobregistration",jobregistration.get_data,methods=["GET"])
app.add_enpoint("/jobinformation/detele","detele jobregistration",jobregistration.delete,methods=["POST"])
# app.add_enpoint("/jobinformation/check_save_job","check_save_job",saveJob.check_save_job,methods=["POST"])


saveJob = SaveJob()
app.add_enpoint("/saveJob/create","create saveJob",saveJob.create,methods=["POST"])
app.add_enpoint("/saveJob/check_save_job","check_save_job",saveJob.check_save_job,methods=["POST"])
app.add_enpoint("/saveJob/get","get saveJob",saveJob.get_data,methods=["GET"])
app.add_enpoint("/saveJob/detele","detele saveJob",saveJob.delete,methods=["POST"])

            


