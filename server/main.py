from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = ""
mongo = PyMongo(app)



@app.route("/")
def hello_world():
    # mongo.db.users.insert_one({"name":"Prince"})
    return "<p>Hello, World!</p>"

app.run(debug=True,port=8000)