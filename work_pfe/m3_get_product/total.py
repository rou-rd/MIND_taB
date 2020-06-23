
from bs4 import BeautifulSoup 
import requests
import json
import pymongo
import datetime

	


def ooredoo():
	URL = 'https://host.ooredoo.tn/nom-de-domaine'
	content = requests.get(URL)
	soup = BeautifulSoup(content.text, 'html.parser')
	text = soup.get_text()
	lenght=len(text)

	
	prices=text[3195:3545]

	thislist = ["HT/an","Commander"]
	for i in list(thislist) :
		prices=prices.replace(i,"")
	prices=prices.split("\n")





	for i in range(0,len(prices)):
		if "DT" in prices[i] and "DT" in prices[i+1]:
			prices[i+1]=""
	while '' in prices:
	    prices.remove('')
	    date=datetime.datetime.today()
	ListeProduct=[]
	mydict={}
	name_product="ooredoo"
	for i in range(0,len(prices),2):
		mydict= { "name_product":name_product, "product": prices[i] , "price" : prices[i+1] , "date":date }
		ListeProduct.append(mydict)

	return(ListeProduct)

def ovh():
	URL = 'https://www.ovh.com/tn/domaines/'
	content = requests.get(URL)
	soup = BeautifulSoup(content.text, 'html.parser')
	text = soup.get_text()
	lenght=len(text)

	thislist = ["Commander","OVHcloudDeals",'""' ,"En savoir plus →","a[","data-tag=","promo", ".pdtBackground","OVHcloudDeals","{ background:","Command", "#59d2ef4d; }","o\"] ","]","HT/ AN","HT/AN"," ",". ","pdtBackground","OVHcloudDeals"]
	prices=text[10555:12000]
	for i in list(thislist) :
		prices=prices.replace(i,"")
	prices=prices.split("\n")
	while '' in prices:
	    prices.remove('')

	while '""' in prices:
	    prices.remove('""')
	    
	    
	for i in prices:
		if len(i)>7 :
			i=i.replace(i[0:6],"")
	date=datetime.datetime.today()
	ListeProduct=[]
	mydict={}
	name_product="ovh"
	for i in range(0,len(prices),2):
		mydict= {"name_product":name_product , "product": prices[i] , "price" : prices[i+1] , "date":date }
		ListeProduct.append(mydict)

	return(ListeProduct)

def atlax():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["prices"]
	mycol = mydb["atlax"]
	URL = 'https://atlax.com/domaines'
	content = requests.get(URL)
	soup = BeautifulSoup(content.text, 'html.parser')
	text = soup.get_text()
	lenght=len(text)
	prices=text[980:1125]
	thislist = ["/an"]
	for i in list(thislist) :
		prices=prices.replace(i,"")

	prices=prices.split("\n")
	while '' in prices:
	    prices.remove('')
	    date=datetime.datetime.today()
	ListeProduct=[]
	mydict={}
	name_product="atlax"
	for i in range(0,len(prices),2):
		mydict= {"name_product":name_product, "product": prices[i] , "price" : prices[i+1] , "date":date }
		ListeProduct.append(mydict)

	return(ListeProduct)

def besthost():
	URL = 'https://besthost.tn/client/cart/?a=add&domain=register&systpl=six'
	content = requests.get(URL)
	soup = BeautifulSoup(content.text, 'html.parser')
	text = soup.get_text()
	lenght=len(text)
	prices=text[26978:27296]
	thislist = ["1 An"]

	for i in list(thislist) :
		prices=prices.replace(i,"")

	prices=prices.split("\n")
	while '' in prices:
	    prices.remove('')
	
	for i in range(20) :
		x="DT"
		
	for i in range(0,len(prices)):
		if "DT" in prices[i] and "DT" in prices[i-1]:
			prices[i-1]=""
	while '' in prices:
	    prices.remove('')

	date=datetime.datetime.today()
	ListeProduct=[]
	mydict={}
	name_product="besthost"
	for i in range(0,len(prices),2):
		mydict= { "name_product":name_product, "product": prices[i] , "price" : prices[i+1] , "date":date }
		ListeProduct.append(mydict)

	return(ListeProduct)

def zenhosting():
	URL = 'https://www.zenhosting.tn/noms-de-domaines-2/'
	content = requests.get(URL)
	soup = BeautifulSoup(content.text, 'html.parser')
	text = soup.get_text()
	lenght=len(text)
	prices=text[5894:5945]
	thislist = ["\n","/an","er","\xa0"]

	for i in list(thislist) :
		prices=prices.replace(i,"")
	prices=prices.split(" ")
	while '' in prices:
	    prices.remove('')
	date=datetime.datetime.today()
	ListeProduct=[]
	mydict={}
	name_product="zenhosting"
	for i in range(0,len(prices),2):
		mydict= {"name_product":name_product, "product": prices[i] , "price" : prices[i+1] , "date":date }
		ListeProduct.append(mydict)

	return(ListeProduct)
