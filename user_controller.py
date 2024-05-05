# any requests are made to controller then sent to model, where the logic would be

from app import app  # file,function
from model.user_model import user_model  # file location, function
from flask import request

obj = user_model()


# read
@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/getall/<id>", methods=["GET"])
def user_getallid_controller(id):
    return obj.user_getallid_model(id)


# create
#data sent frompostman is sent to python env,
# to send it to sql update code in user_model
@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    #print(request.form)
    return obj.user_addone_model(request.form)
#this request.from goes to data (self,data) in function


#UPDATE
@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    #print(request.form)
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)

#pagination,  getting data based on page number and limit of rows on that page
@app.route("/user/getall/limit/<limit>/page/<page>", methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)

