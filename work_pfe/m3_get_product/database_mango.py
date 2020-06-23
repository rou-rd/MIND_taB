import pymongo
import total as ss
import sys
url="mongodb://localhost:27017/"
name_database="mydatabase"
name_table="application_conccurent"

myclient = pymongo.MongoClient(url)
"""create a new databse  """
mydb = myclient[name_database]
""" create a new collection=table"""
mycol = mydb[name_table]

##show the list of collections_names= lister les noms des tables
def list_of_collection():
	return mydb.list_collection_names()
## check if the collection exist in the database
def check_collection_name(name_collection):
	verif=False
	list_col=list_of_collection(mydb)
	if name_collection in list_col:
		verif=True
	return verif


##insert a document un a collection = inserer des lignes dans un tableau
def insert_document_list(list_data,name_collection):
	mycol = mydb[name_collection]
	ids=mycol.insert_many(list_data)
	print(ids)
	

##insert a document un a collection = inserer une ligne dans un tableau
def insert_document(mydict,name_collection):
	mycol = mydb[name_collection]
	x = mycol.insert_one(mydict)


def check_collection_dict(dict_data):
	x=False
	for x in mycol.find():
		if x['name']==dict_data['name']:
			x=True
	return x

##to show all document in a collection = voir tout les lignes dans un tableau
def show_collection(name_collection):
	mycol = mydb[name_collection]
	liste=[]
	for x in mycol.find():
		liste.append(x)
	return liste

## show the last id of last document 
def show_the_last_id(name_collection):
	d=0
	mycol = mydb[name_collection]
	for x in mycol.find():
		d=x['id']
	return d

## To delete all documents in a collection = supprimer tout les lignes dans un tableau  		
def delete_all_doc_in_coll(name_collection):
	mycol = mydb[name_collection]
	x = mycol.delete_many({})
	print(x.deleted_count, " documents deleted.") 


def check_data_duplicate_db(data,name_collection):
	dep=False
	mycol = mydb[name_collection]
	for x in mycol.find():
		if((data['price']==x['price'])and(data['product']==x['product'])and(data['date']==x['date'])):
			dep=True
	return dep

def check_data_duplicate_db_by_name(data,name_collection):
	dep=False
	mycol = mydb[name_collection]
	for x in mycol.find():
		if(data['name']==x['name']):
			dep=True
	return dep
def delete_collection(name_collection):
	mycol = mydb[name_collection]
	mycol.drop()
	print("collection deleted")
"""
def static_data(name_collection,name_collection_static_data):
	print("hello")
	mycol = mydb[name_collection]
	mycol_static_data = mydb[name_collection_static_data]
	for d1 in mycol.find():
		if(check_data_duplicate_db_by_name(d1,"data_static")==True):
			mydict={"name":d1["name"],"total":0}
			insert_document(mydict,"data_static")
			
"""


def main_db(product):
	for xx in product:
		the_last_id=show_the_last_id("product_products")
		xx['id']=the_last_id+1
		print(xx)
		if(check_data_duplicate_db(xx,"product_products")==False):
			insert_document(xx,"product_products")

main_db(ss.ooredoo())
main_db(ss.ovh())
main_db(ss.atlax())
main_db(ss.zenhosting())
main_db(ss.besthost())

"""
##insert_document_list(datas,"application_conccurent")



##the_last_id=show_the_last_id("application_conccurent")

delete_all_doc_in_coll("application_conccurent")




"""
