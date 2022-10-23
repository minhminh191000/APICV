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
                info = PersonalInformation(userpublic_id,fullname=data.get("fullname"),birth_of_day=data.get("birth_of_day"),gender=data.get("gender"),phone=data.get("phone"),address=data.get("address"))
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
                info.phone = data.get("phone")
                info.address = data.get("address")
                db.session.commit()
                return jsonify({"status":200,"message":"Updated successfully"})
            else:
                return jsonify({"status":404,"message":"update fail"})


class InformationController:


    # thong tin nguoi dung
    @jwt_required()
    def create(self):
        if request.method == "POST":
            # lay thon tin tu fontend tra ve
                data = request.get_json()
                userpublic_id = get_current_user().id
                personalinformation = db.session.query(PersonalInformation).filter(PersonalInformation.userpublic_id == userpublic_id).first()
                personalinformation_id = personalinformation.id 
                name = data.get("name")
                title_1 = data.get("title_1")
                title_2 = data.get("title_2")
                date_in = data.get("date_in")
                date_out = data.get("date_out")
                description_details = data.get("description_details")
                # information = Information()
                information = Information(name,title_1,title_2,date_in,date_out,description_details,personalinformation_id)
                db.session.add(information)
                db.session.commit()
                return jsonify({"status":200,"message":"Create information"})

    @jwt_required()
    def update(self):
         if request.method == "PUT":
            try :
                data = request.get_json()
                userpublic_id = get_current_user().id
                record_id = data.get("id")



                personalinformation = db.session.query(PersonalInformation).filter(PersonalInformation.userpublic_id == userpublic_id).first()
                information = db.session.query(Information).filter(Information.id == record_id).first()
                if information.personalinformation_id == personalinformation.id :
                    information.name = data.get("name")
                    information.title_1 = data.get("title_1")
                    information.title_2 = data.get("title_2")
                    information.date_in = data.get("date_in")
                    information.ate_out = data.get("date_out")
                    information.description_details = data.get("description_details")
                    db.session.commit()
                    return  jsonify({"status":200,"message":"Updated information"})
                else :
                    return  jsonify({"status":404,"message":"User does not have permission"})
            except :
                return  jsonify({"status":404,"message":"recrd error !"})
    @jwt_required()
    def get(self):
        userpublic_id = get_current_user().id
        personalinformation = db.session.query(PersonalInformation).filter(PersonalInformation.userpublic_id == userpublic_id).first()
        information = db.session.query(Information).filter(Information.personalinformation_id == personalinformation.id).all()
        if information is not None:
            list_information = []
            for item in information:
                list_information.append(item.obj_person())
            return jsonify({"status":200,"data":list_information,"message":"records"})
        else:
            return jsonify({"status":200,"data":[],"message":"There are no records"})

    
    @jwt_required()
    def delete(self):
        if request.method == "POST":
            data = request.get_json()
            information = db.session.query(Information).filter(Information.id == data.get("id")).first()
            if information is not None:
                db.session.delete(information)
                db.session.commit()
                return jsonify({"status":200,"message":"Delete information successfully"})
            return jsonify({"status":404,"message":"Delete information fail"})        

            
            


info = PersonalInformationController()

app.add_enpoint("/user/create_perinfo","create info",info.create,methods=["POST"])
app.add_enpoint("/user/get_info","show info",info.get_info,methods=["GET"])
app.add_enpoint("/user/update","update info",info.update,methods=["PUT"])


infomation = InformationController()
# app.ad
app.add_enpoint("/infomation/create","create_infomation",infomation.create,methods=["POST"])
app.add_enpoint("/infomation/update","update_infomation",infomation.update,methods=["PUT"])
app.add_enpoint("/infomation/get","get_infomation",infomation.get,methods=["GET"])
app.add_enpoint("/infomation/delete","delete_infomation",infomation.get,methods=["POST"])

            


