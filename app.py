from flask import Flask
from controller.FlaskAppWrapper import FlaskAppWrapper
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager



flask_app = Flask(__name__)


# Setup the Flask-JWT-Extended extension
flask_app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(flask_app)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@flask_app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    print(username,password)
    login = db.session.query(UserPublic).filter(UserPublic.username == username).first()
    if login:
        if login.password == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token) 
    return jsonify({"msg": "Bad username or password"}), 401



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
    # 'SQLALCHEMY_DATABASE_URI':'postgresql://qvoszmzjeubaam:09d3769eb47b52f41a3f70b5b259566b8f90be9f893b0c14035c3c916b4d96ff@ec2-52-200-5-135.compute-1.amazonaws.com:5432/d4adufef73bonr',
    'SQLALCHEMY_DATABASE_URI':'postgresql://flask_user:1@localhost:5432/flask_cv',
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
# from controller.Auth import *
# from controller.EmpController import *



# import model

# from model.Employee import *
from model.user_cv import *
from model.personal_information import *
# test = ViewController()

# app.add_enpoint("/","test",test.index)





if __name__ == "__main__":
    app.run(debug=True)