from app import app ,db,get_current_user
from flask import jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity


from model.job_registration import JobRegistration as Job 

import json
# from app import db,app
# from model.personal_information import *

class JobRegistration:


    @jwt_required()
    def get_data(self):
        user = get_current_user()
        # print("user ======",user.id)
        job_registration = db.session.query(Job).filter(Job.user_id == user.id).all()
        print(job_registration)
        list_job = []
        for job in job_registration:
            
            vals = {
                        "id":job.id,
                        "job_id":job.job_id,
                        "user_id":job.user_id,
                        "name":self.get_job(job.job_id)
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
        for i in json_object:
            if int(i["id"]) == int(id):
                return i["name"]
        

            





jobregistration = JobRegistration()
# # app.ad
app.add_enpoint("/jobinformation/create","create jobregistration",jobregistration.create,methods=["POST"])
app.add_enpoint("/jobinformation/get","get jobregistration",jobregistration.get_data,methods=["GET"])
app.add_enpoint("/jobinformation/detele","detele jobregistration",jobregistration.delete,methods=["POST"])

            


