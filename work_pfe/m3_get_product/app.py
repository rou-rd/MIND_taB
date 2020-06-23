#!flask/bin/python
from flask import Flask, jsonify ,make_response,request
from flask_pymongo import PyMongo


app = Flask("__name__")

app.config["MONGO_DBNAME"] = "prices"
app.config["MONGO_URI"] = "mongodb://localhost:27017/prices"

mongo = PyMongo(app)

@app.route('/') #to check whether the application is running correctly on port
def hello_world():
    return 'flask is running correctly'

@app.route('/prices/2/atlax', methods=['GET']) 
def get_price1_atlax():
	price = mongo.db.atlax
	prices = []
	price = price.find()
	for j in price:
		j.pop('_id')
		prices.append(j)
	return jsonify({'datas': prices})	

@app.route('/prices/ovh', methods=['GET']) 
def get_price_ovh():
	price = mongo.db.ovh
	prices = []
	price = price.find()
	for j in price:
		j.pop('_id')
		prices.append(j)
	return jsonify({'datas': prices})	
@app.route('/prices/ooredoo', methods=['GET']) 
def get_price_ooredoo():
	price = mongo.db.ooredoo
	prices = []
	price = price.find()
	for j in price:
		j.pop('_id')
		prices.append(j)
	return jsonify({'datas': prices})

@app.route('/prices/besthost', methods=['GET']) 
def get_price_besthost():
	price = mongo.db.besthost
	prices = []
	price = price.find()
	for j in price:
		j.pop('_id')
		prices.append(j)
	return jsonify({'datas': prices})	

@app.route('/prices/zenhosting', methods=['GET']) 
def get_price_zenhosting():
	price = mongo.db.zenhosting
	prices = []
	price = price.find()
	for j in price:
		j.pop('_id')
		prices.append(j)
	return jsonify({'datas': prices})	





if __name__ == "__main__":
    app.debug = True
    app.run()
