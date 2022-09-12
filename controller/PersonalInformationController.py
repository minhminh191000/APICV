from app import app ,db,get_current_user
from flask import jsonify,json,request
from flask_jwt_extended import jwt_required,get_jwt_identity
# from app import db,app
from model.personal_information import *

class PersonalInformationController:

    @jwt_required()
    def get_info(self):
        userpublic_id = get_current_user().id
        info = db.session.query(PersonalInformation).filter(PersonalInformation.userpublic_id == userpublic_id).first()
        if info is not None:
            return jsonify({"status":200,"data":info.obj_person(),"message":"records"})
        else:
            return jsonify({"status":200,"data":[],"message":"There are no records"})
        
        # result = []
        # for i in query:
        #     result.append(i.obj_person())
        # return jsonify({"status":200,"data":result})

        # pass
    @jwt_required()
    def create(self):
        # current_user = get_jwt_identity()
        if request.method == "POST":
            # user = db.session.query(UserPublic).filter(UserPublic.username == current_user).first()
            data = request.get_json()
            userpublic_id = get_current_user().id
            
            if db.session.query(PersonalInformation).filter(PersonalInformation.userpublic_id == userpublic_id).first() is not None:
                return jsonify({"status":404,"message":"already exist info"})
            else:
                info = PersonalInformation(userpublic_id,fullname=data.get("fullname"),birth_of_day=data.get("birth_of_day"),gender=data.get("gender"))
                db.session.add(info)
                db.session.commit()
                return jsonify({"status":200,"message":"Create info"})
        return  jsonify({"status":400,"message":"fail"})

    @jwt_required()
    def update(self):
         if request.method == "PUT":
            data = request.get_json()
            userpublic_id = get_current_user().id
            info = db.session.query(PersonalInformation).filter(PersonalInformation.userpublic_id == userpublic_id).first()
            # print(info.name)
            if info is not None:
                info.fullname = data.get("fullname")
                info.address = data.get("birth_of_day")
                info.email = data.get("gender")
                db.session.commit()
                return jsonify({"status":200,"message":"Updated successfully"})
            else:
                return jsonify({"status":404,"message":"update fail"})



info = PersonalInformationController()

app.add_enpoint("/user/create_perinfo","create info",info.create,methods=["POST"])
app.add_enpoint("/user/get_info","show info",info.get_info,methods=["GET"])
app.add_enpoint("/user/update","update info",info.update,methods=["PUT"])
# app.add_enpoint("/user/create","create_user",UserCV.create_user,methods=["POST"])

            


