
from flask import jsonify,json,request
from flask_login import login_required

from model.Employee import *

from app import db,app,process_data


class EmpController:

    @login_required
    def add_employee(self):
        if request.method == "POST":
            data = request.get_json()
            if self.email_duplicate(data.get("email")):
                return jsonify({"status":"fail","message":"Email already exists"})
            employee = Employee(name=data.get("name"),email=data.get("email"),address=data.get("address"),
                            file_name=data.get("file_name"))
            db.session.add(employee)
            db.session.commit()
            return jsonify({"status":"successfully","data":employee.obj_person()})
    @login_required
    def update_employee(self):
        if request.method == "PUT":
            data = request.get_json()
            filter_id = data.get("id")
            emp = db.session.query(Employee).filter(Employee.id == filter_id).first()
            if emp is not None:
                emp.name = data.get("name")
                emp.address = data.get("address")
                emp.email = data.get("email")
                emp.file_name = data.get("file_name")
                db.session.commit()
                return jsonify({"status":"successfully","message":"Updated successfully"})
            else:
                return jsonify({"status":"fail","message":"update fail"})


    @login_required
    def show_all_employee(self):
        employees = db.session.query(Employee).all()
        # print(employee)
        if employees is not None:
            return jsonify({"status":"successfully","data":process_data(employees)})
        return jsonify({"status":"fail","data":{}})

    @login_required
    def delete_employee(self):
        if request.method == "POST":
            data = request.get_json()
            employee = db.session.query(Employee).filter(Employee.id == data.get("id")).first()
            if employee is not None:
                db.session.delete(employee)
                db.session.commit()
                return jsonify({"status":"successfully","message":"Delete employee successfully"})
            return jsonify({"status":"fail","message":"Delete employee fail"})
    @login_required
    def get_by_id(self):
        if request.method == "POST":
            data = request.get_json()
            emp = db.session.query(Employee).filter(Employee.id == data.get("id")).first()
            if emp is not None:
                return jsonify({"status":"successfully","data":emp.obj_person()})
            else:
                return jsonify({"status":"fail","data":{}})



    def email_duplicate(self,email):
        data = db.session.query(Employee).filter(Employee.email == email).first()
        if data is not None:
            return True
        return False



# employee = EmpController()

# app.add_enpoint("/add_employee","add_employee",employee.add_employee,methods=["POST"])
# app.add_enpoint("/show_all_employee","show_all_employee",employee.show_all_employee,methods=["GET"])
# app.add_enpoint("/delete_employee","employee",employee.delete_employee,methods=["POST"])
# app.add_enpoint("/update_employee","update_employee",employee.update_employee,methods=["PUT"])
# app.add_enpoint("/get_by_id","get_by_id",employee.get_by_id,methods=["POST"])