#!flask/bin/python
from flask import Flask, jsonify ,make_response,request
from flask_pymongo import PyMongo


app = Flask("__name__")

app.config["MONGO_DBNAME"] = "mydatabase"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"

mongo = PyMongo(app)

@app.route('/') #to check whether the application is running correctly on port
def hello_world():
    return 'flask is running correctly'

@app.route('/conccurentList', methods=['GET']) #viewing all contents of bucketList
def get_conccurentList():
	conccurent = mongo.db.application_conccurent
	conccurents = []
	conccurent = conccurent.find()
	for j in conccurent:
		j.pop('_id')
		conccurents.append(j)
	return jsonify({'datas': conccurents})	




if __name__ == "__main__":
    app.debug = True
    app.run()