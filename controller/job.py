from app import app ,db,get_current_user
from flask import jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity

import json
# from app import db,app
# from model.personal_information import *

class JobInformation:

    def get_all_paging(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)

        obj_result = self.paging(page_id,result_per_page,json_object)
        return jsonify({"status":200,"data":obj_result})
        
    def search_job(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")

        
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)





    def paging(self,page_id,result_per_page,json_object):
        page = int(page_id) if page_id is not None else 1
        result_per_page = int(result_per_page) if result_per_page is not None else 5
        data_job = json_object[(page-1)*result_per_page:(page-1)*result_per_page + result_per_page] 
        obj_result = {
            'page':page,
            "result_per_page":result_per_page,
            "total":len(data_job),
            "data": data_job
        }
        return obj_result

    
            





jobinformation = JobInformation()
# # app.ad
# app.add_enpoint("/infomation/create","create_infomation",infomation.create,methods=["POST"])
# app.add_enpoint("/infomation/update","update_infomation",infomation.update,methods=["PUT"])
app.add_enpoint("/jobinformation/get_all","get_all",jobinformation.get_all_paging,methods=["GET"])
# app.add_enpoint("/infomation/delete","delete_infomation",infomation.get,methods=["POST"])

            


