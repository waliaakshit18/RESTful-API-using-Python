from flask import Flask

app =Flask(__name__)

@app.route("/")
def welcome():
    return "Hi"

@app.route("/home")
def home():
    return "you found me"

from controller import user_controller
