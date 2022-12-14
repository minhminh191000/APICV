from app import app ,db
from flask import jsonify,json,request
from flask_jwt_extended import jwt_required
# from app import db,app
from model.user_cv import *
from model.personal_information import *
from controller.PersonalInformationController import *

class UserCVController:

    @jwt_required()
    def get_all_user(self):
        query = db.session.query(UserPublic).all()
        result = []
        for i in query:
            result.append(i.obj_person())
        return jsonify({"status":200,"data":result})

    def create_user(self):
        if request.method == "POST":
            data = request.get_json()
            if self.email_duplicate(data.get("email")):
                return jsonify({"status":"fail","message":"Email already exists"})
            user = UserPublic(username=data.get("username"),email=data.get("email"),password=data.get("password"))
            db.session.add(user)
            db.session.commit()
            info = PersonalInformation(user.id,fullname="nguyen van A",birth_of_day=None,gender="Nam",phone="0123456789",address="Ha Noi",position=None,about=None,skills=None,avatar_url = 'https://vnn-imgs-a1.vgcloud.vn/image1.ictnews.vn/_Files/2020/03/17/trend-avatar-1.jpg',resumeUrl=None)
            # info = PersonalInformation(userpublic_id,fullname=data.get("fullname"),birth_of_day=data.get("birth_of_day"),gender=data.get("gender"),phone=data.get("phone"),address=data.get("address"),position=data.get("position"),about=data.get("about"),skills=data.get("skills"),avatar_url=data.get("avatar_url"))

            db.session.add(info)
            db.session.commit()
            return jsonify({"status":200,"message":"Create USER"})
        return  jsonify({"status":400,"message":"fail"})

    def email_duplicate(self,email):
        data = db.session.query(UserPublic).filter(UserPublic.email == email).first()
        if data is not None:
            return True
        return False



UserCV = UserCVController()

app.add_enpoint("/user/get_all","get_all_user",UserCV.get_all_user,methods=["GET"])
app.add_enpoint("/user/create","create_user",UserCV.create_user,methods=["POST"])

            


