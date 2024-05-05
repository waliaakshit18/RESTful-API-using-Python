# response of the request are sent from here
import json

import mysql.connector  # connection gateway to be opened by this for connec b/w mysql,python
from flask import make_response


class user_model():

    # connection establishment code written here, instead writing them for every function
    # exectuted after object initialisation in user file and connection made
    def __init__(self):
        try:
            self.c = mysql.connector.connect(host="localhost", user="root", password="", database="flask_project")
            self.c.autocommit = True
            self.curr = self.c.cursor(dictionary=True)  # data shown in form of dict
            print("fine")
        except:
            print("error")

    # (self )is used to use functions declared in one function and use in another beyond its scope

    # query execution code

    # read
    def user_getall_model(self):
        self.curr.execute("SELECT * from user")
        result = self.curr.fetchall()  # gives all the result queries of user table
        print(result)  # prints in terminal

        if len(result) > 0:
            return {"payload": result}  # list to dictionary(key-value) application/json
        # return json.dumps(result)# this returns list in text/html as string(coverted from list) form in postman
        # returns in browser, but dumps is used to convert in stringify, conveert in stringd,#its [{} ],  dictionary[{list, one row of sql table} ]
        else:
            return {"message": "No data found"}  # string changed to dictionary

    def user_getallid_model(self, id):
        self.curr.execute(f"SELECT* from user WHERE id={id}")
        result = self.curr.fetchone()
        if len(result) > 0:
            return {"payload": result}
        else:
            return {"message": "No data found"}

    # create
    # -->  data is sent from browser to sql, http request of data sent to server of sql
    # data travles from postman to controller and then to model
    def user_addone_model(self, data):
        self.curr.execute(
            f"INSERT into user(name,email,phone,role,password) VALUES( '{data['name']}',' {data['email']}',' {data['phone']}',' {data['role']}',' {data['password']}' ) ")
        # print(data)
        # print(data['phone'])   for specific vallue
        return {"message": "This is user_addone_model"}

    # UPDATE
    def user_update_model(self, data):
        self.curr.execute(
            f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}")
        if self.curr.rowcount > 0:
            return {"message": "User updated successfully"}
        else:
            return {"message": "No user updated"}

    def user_delete_model(self, id):
        self.curr.execute(f"DELETE from user where id={id}")
        if self.curr.rowcount > 0:
            return {"message": "User deleted successfully"}
        else:
            return {"message": "Nothing to delete"}

    def user_pagination_model(self, limit, page):

        # limit subtracted so that we get start point, page*limit kind of gives
        # serial number of content on that page
        # converting string format into int
        page = int(page)
        limit = int(limit)
        start = (page * limit) - limit
        qry = f"SELECT * from user LIMIT {start},{limit}"
        self.curr.execute(qry)
        result = self.curr.fetchall()
        if len(result) > 0:
            return make_response({"payload": result})
        else:
            return make_response("No data available")
