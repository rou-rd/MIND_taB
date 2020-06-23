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

@app.route('/prices/', methods=['GET']) 
def get_price():
	price = mongo.db.product_products
	prices = []
	price = price.find()
	for j in price:
		j.pop('_id')
		prices.append(j)
	return jsonify({'datas': prices})	




if __name__ == "__main__":
    app.debug = True
    app.run()
