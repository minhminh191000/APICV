from flask import request,json,jsonify
from flask_login import login_user,login_required,logout_user,current_user
# login_manager.login_view = 'login'


from app import db,app

from model.User import *

class Authenticate:

    def login(self):
        if request.method == "POST":
            data = request.get_json()
            username = data.get('username')
            password = data.get('passwd') 
            user =db.session.query(User).filter(User.username == username,User.passwd == password).first()
            print("hello ",user)
            if user:
                login_user(user)
                return jsonify(user.obj_person())
            else:
                return jsonify({"status": 401,
                                "message": "Username or Password Error"})
        return jsonify({"status": 404,
                                "message": "No Login"})

    @login_required
    def logout(self):
        logout_user()
        return jsonify({"status":"successfully","message":"Logout successfully"})
    @login_required
    def test(self):
        return jsonify({"status":"successfully","user":current_user.username})
    

# auth = Authenticate()
# app.add_enpoint("/login","login",auth.login,methods=["POST"])
# app.add_enpoint("/test","test",auth.test,methods=["GET"])
# app.add_enpoint("/logout","logout",auth.logout)


