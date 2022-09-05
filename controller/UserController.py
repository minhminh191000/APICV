from flask import request,json,jsonify

from flask_login import login_required


from app import db,app,process_data
from model.Employee import Employee


from model.User import *


class UserController:

    #add user
    @login_required
    def add_user(self):
        if request.method == "POST":
            data = request.get_json()
            if data is not None:
                email = data.get("email")
                username = data.get("username")
                passwd = data.get("passwd")
                user = User(email,username,passwd)
            try:
                db.session.add(user)
                db.session.commit()
                return jsonify({"status":"successfully","message":"ADDED USER SUCCESSFULLY"})
            except Exception as e:
                return jsonify({"status":"fail","message":"ADD USER FAILED"})
        return jsonify({"status":"error","message":"NO METHOS POST"})
    # @login_required
    def show_all(self):
        results_data = db.session.query(User).all()
        return jsonify({"status":"successfully","data":process_data(results_data)})
    @login_required
    def change_email(self):
        if request.method == "PUT":
            data = request.get_json()
            filter_name = data.get("username")
            record = db.session.query(User).filter(User.username == filter_name).first()
            if data is None:
                return jsonify({"status":"fail","message":"No records found"})
            else:
                record.email = data.get("email_new")
                db.session.commit()
                return jsonify({"status":"successfully","message":"Updated successfully"})
    @login_required
    def change_passwd(self):
        if request.method == "PUT":
            # record = None
            data = request.get_json()
            filter_name = data.get("username")
            record = db.session.query(User).filter(User.username == filter_name).first()
            if record is None:
                return jsonify({"status":"fail","message":"No records found"})
            else:
                # print("=============", record.passwd)
                if data.get("passwd_old") == record.passwd:
                    record.passwd = data.get("passwd_new")
                    db.session.commit()
                    return jsonify({"status":"successfully","message":"Updated passwd successfully"})
                else:
                    return jsonify({"status":"fail","message":"entered wrong password"})
    # def paging(self):
    #     page = int(request.args.get())            
    # def process_data(self,results):
    #     list_result = []
    #     for item in results:
    #         list_result.append(item.obj_person())
    #     return list_result




# usercontroller = UserController()

# app.add_enpoint("/add_user","add_user",usercontroller.add_user,methods=["POST"])
# app.add_enpoint("/show_all","show_all_user",usercontroller.show_all,methods=["GET"])
# app.add_enpoint("/change_email","change_email",usercontroller.change_email,methods=["PUT"])
# app.add_enpoint("/change_passwd","change_passwd",usercontroller.change_passwd,methods=["PUT"])

