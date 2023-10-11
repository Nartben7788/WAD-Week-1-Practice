from flask import Flask
renderapp=Flask(__name__)
@renderapp.route("/")
def home():
    return "Hello world"
