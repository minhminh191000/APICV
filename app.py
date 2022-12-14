# from datetime import timedelta

from flask import Flask
from controller.FlaskAppWrapper import FlaskAppWrapper
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import set_access_cookies
# from flask_jwt_extended import set_access_cookies
# import redis

from datetime import datetime
from datetime import timedelta
from datetime import timezone


# ACCESS_EXPIRES = timedelta(hours=1)


flask_app = Flask(__name__)

flask_app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
# Setup the Flask-JWT-Extended extension
flask_app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
flask_app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
# flask_app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(flask_app)


# @flask_app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.datetime.now(timezone.utc)
#         # now = datetime.now
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=120))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             set_access_cookies(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original response
#         return response


@flask_app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # print(username,password)
    login = db.session.query(UserPublic).filter(UserPublic.username == username).first()
    if login:
        if login.password == password:
            response = jsonify({"msg": "login successful"})
            access_token = create_access_token(identity=username)
            set_access_cookies(response, access_token)
            return jsonify(access_token=access_token) 
    return jsonify({"msg": "Bad username or password"}), 401




@flask_app.route("/logout", methods=["POST"])
def logout_with_cookies():
    response = jsonify({"status":200,"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response





# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@flask_app.route("/get_current_user", methods=["GET"])
@jwt_required()
def get_current_user():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    current_user = db.session.query(UserPublic).filter(UserPublic.username == current_user).first()
    return current_user



# SQLALCHEMY_DATABASE_URI': 'mysql://root:Minh123456@127.0  .0.1:3306/flask_app
# postgres://qvoszmzjeubaam:09d3769eb47b52f41a3f70b5b259566b8f90be9f893b0c14035c3c916b4d96ff@ec2-52-200-5-135.compute-1.amazonaws.com:5432/d4adufef73bonr
obj = {
    'SECRET_KEY':'secret-key-goes-here',
    'SQLALCHEMY_DATABASE_URI':'postgresql://qvoszmzjeubaam:09d3769eb47b52f41a3f70b5b259566b8f90be9f893b0c14035c3c916b4d96ff@ec2-52-200-5-135.compute-1.amazonaws.com:5432/d4adufef73bonr',
    # 'SQLALCHEMY_DATABASE_URI':'postgresql://flask_user:1@localhost:5432/flask_cv',
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "MAX_CONTENT_LENGTH":500*1000*1000,
}

app = FlaskAppWrapper(flask_app,obj)

db = app.db
# jwt = JWT(app, self.authenticate, self.identity)

# import controller 
from controller.HomeController import *
from controller.UserCVController import *
from controller.PersonalInformationController import *
from controller.job import *
from controller.job_registration import *
# from controller.Auth import *
# from controller.EmpController import *



# import model

# from model.Employee import *
from model.user_cv import *
from model.personal_information import *
from model.frofession import *
from model.job_registration import *
# test = ViewController()

# app.add_enpoint("/","test",test.index)





if __name__ == "__main__":
    app.run(debug=True)