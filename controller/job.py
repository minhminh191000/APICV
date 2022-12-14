from app import app ,db,get_current_user
from flask import jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity
import random

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
        return obj_result
    
    def get_random(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)
        # print(json_object) 
        random.shuffle(json_object)
        # print(json_object)
        obj_result = self.paging(page_id,result_per_page,json_object)
        return jsonify({"status":200,"data":obj_result})



    def get_salary(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)



        salary = []
        for item in json_object:
                job_details =  item["job_details"]
                for i in job_details:
                    salary.append(i["general_information"]["salary"])
        salary = set(salary)
        salary = list(salary)
        

        # obj_result = self.paging(page_id,result_per_page,json_object)
        return jsonify({"status":200,"data":salary})

    def get_profession_all(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        with open('controller/profession.json', 'r') as openfile:
            json_object = json.load(openfile)



        profession = []
        for item in json_object:

            vals = {
                    "name":item["name"],
                    "id":item["id"]
                    }
            profession.append(vals)
        # profession = set(profession)
        # profession = list(profession)
        

        # obj_result = self.paging(page_id,result_per_page,json_object)
        return jsonify({"status":200,"data":profession})


    
    # detail
    def detail_job(self,id):
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)

        for item in json_object:
            if int(item["id"]) == int(id): 
                # print("item")
                
                return jsonify({"status":200,"data":item})
        return jsonify({"status":404,"data":[]})
        


    def search_job(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        # job = []
        flag = 0
        for i in request.args.keys():
            flag = 1
            if i == 'name':
                name = request.args.get("name")
                # job.append(self.check_job(i,name))
                job = self.check_job(i,name)

            if i == "location":
                location = request.args.get("location")
                # job.append(self.check_job(i,location))
                job = self.check_job(i,location)


            if i == "profession":
                profession_id = request.args.get("profession")
                # job.append(self.check_job(i,profession_id))
                job = self.check_job(i,profession_id)
                
                
            if i == "salary":
                salary = request.args.get("salary")
                # job.append(self.check_job(i,salary))
                job = self.check_job(i,salary)

        if flag == 1: 
            obj_result = self.paging(page_id,result_per_page,job)
            return obj_result
        else:
            with open('controller/DataFrofession.json', 'r') as openfile:
                json_object = json.load(openfile)
            obj_result = self.paging(page_id,result_per_page,json_object)
            return obj_result







    def get_all_company(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        with open('controller/Company.json', 'r') as openfile:
            json_object = json.load(openfile)
        obj_result = self.paging(page_id,result_per_page,json_object)
        return obj_result


    def get_detail(self,id):
        company = []
        with open('controller/Company.json', 'r') as openfile:
            json_object = json.load(openfile)
        for i in json_object:
            if i["id"] == id:
                company.append(i)
        return jsonify({"status":200,"data":company})

    def get_job_company(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        company_id = request.args.get("company_id")

        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)


        list_job = []
        for job in json_object:
            # print(job)
            # print(job["id"])
            if company_id == job["company_id"]:
                list_job.append(job)

        obj_result = self.paging(page_id,result_per_page,list_job)
        return jsonify({"status":200,"data":obj_result})
    # def search_company(self):







    def get_profession(self):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        with open('controller/profession.json', 'r') as openfile:
            json_object = json.load(openfile)
        obj_result = self.paging(page_id,result_per_page,json_object)
        return jsonify({"status":200,"data":obj_result})


    def get_profession_detail(self,id):
        page_id = request.args.get("page")
        result_per_page = request.args.get("result_per_page")
        profession = []
        with open('controller/profession.json', 'r') as openfile:
            json_object = json.load(openfile)
        for i in json_object:
            # print(i["id"])
            
            # print(i)
            if i["id"] == id:
                for detailed_occupation in i["detailed_occupation"]:
                    print(detailed_occupation)
            #         print(detailed_occupation)
                    profession.append(detailed_occupation)
        obj_result = self.paging(page_id,result_per_page,json_object)
        return jsonify({"status":200,"data":profession})

# get_profession,get_profession_detail














    def check_job(self,key,value):
        with open('controller/DataFrofession.json', 'r') as openfile:
            json_object = json.load(openfile)
        job = []
        if key == "name" or key == "profession" :
            for item in json_object:
                # print( " da vao day r ")
                if item[key].lower() in value.lower(): 
                    # print( " da vao ")
                    job.append(item)
            return job
        elif key == "location":
            for item in json_object:
                job_details =  item["job_details"]
                for i in job_details:
                    for location in i[key]:
                        if location.lower() == value.lower():
                            job.append(item)
            return job
        elif key == "salary":
            for item in json_object:
                job_details =  item["job_details"]
                for i in job_details:
                    if str(i["general_information"]["salary"].lower()) == str(value.lower()):

                        job.append(item)       
            return job


        





    def paging(self,page_id,result_per_page,json_object):
        page = int(page_id) if page_id is not None else 1
        result_per_page = int(result_per_page) if result_per_page is not None else 5
        data_job = json_object[(page-1)*result_per_page:(page-1)*result_per_page + result_per_page] 
        print(data_job)
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
app.add_enpoint("/jobinformation/get_random","get_random",jobinformation.get_random,methods=["GET"])
app.add_enpoint("/jobinformation/detail_job/<int:id>","detail_job",jobinformation.detail_job,methods=["GET"])
app.add_enpoint("/jobinformation/search_job","search_job",jobinformation.search_job,methods=["GET"])
# app.add_enpoint("/jobinformation/get_all","get_all",jobinformation.get_all_paging,methods=["GET"])
# app.add_enpoint("/infomation/delete","delete_infomation",infomation.get,methods=["POST"])
# get_all_company


# get_profession,get_profession_detail
app.add_enpoint("/company/get_all","get_all_company",jobinformation.get_all_company,methods=["GET"])
app.add_enpoint("/company/get_job_company","get_job_company",jobinformation.get_job_company,methods=["GET"])
app.add_enpoint("/company/get_job_company/<id>","get_detail",jobinformation.get_detail,methods=["GET"])


app.add_enpoint("/profession/get_all","get_profession",jobinformation.get_profession,methods=["GET"])
app.add_enpoint("/profession/profession_detail/<id>","profession_detail",jobinformation.get_profession_detail,methods=["GET"])
# app.add_enpoint("/profession/profession_detail/<id>","profession_detail",jobinformation.get_profession_detail,methods=["GET"])



app.add_enpoint("/jobinformation/get_salary","get_salary",jobinformation.get_salary,methods=["GET"])
app.add_enpoint("/profession/get_profession","get_profession_all",jobinformation.get_profession_all,methods=["GET"])
# get_profession
            


