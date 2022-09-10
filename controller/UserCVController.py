from app import app ,db
from flask import jsonify,json,request
from flask_jwt_extended import jwt_required
# from app import db,app
from model.user_cv import *

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

            


