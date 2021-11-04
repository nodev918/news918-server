from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>news918 新聞發布系統</p>"

@app.route("/write",methods=["GET","POST"])
def upload():
    print("write to mongoDB")
    client = MongoClient("mongodb+srv://yale918:12345@cluster0.ym9ma.mongodb.net/newsdb?retryWrites=true&w=majority")
    db = client.newsdb

    col = db["news"]

    data_list = [
        { "name":"Amy"},
        { "name":"Yale"}
    ]

    col.insert_many(data_list)