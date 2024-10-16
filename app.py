import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)


# url untuk home
@app.route("/")
def home():
    return render_template("index.html")


# url untuk message
@app.route("/message", methods=["POST"])
def message_post():
    name_receive = request.form["name_give"]
    email_receive = request.form["email_give"]
    message_receive = request.form["message_give"]

    doc = {
        "name": name_receive,
        "email": email_receive,
        "message": message_receive,   
    }

    # menambahkan data ke collection
    db.messages.insert_one(doc)

    return jsonify({"msg": "Thanks for the message!!!"})

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

