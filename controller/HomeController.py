from app import app ,db
from flask import jsonify,json,request


class HomeController:


    def home(self):
        return jsonify({"status":200,"mesages":"Welcome to Migor"})

main = HomeController()

app.add_enpoint("/","home",main.home)
