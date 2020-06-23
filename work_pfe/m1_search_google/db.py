
import pymongo
import search as ss
url="mongodb://localhost:27017/"
name_database="mydatabase"
name_table="application_conccurent"

myclient = pymongo.MongoClient(url)
"""create a new databse  """
mydb = myclient[name_database]
""" create a new collection=table"""
mycol = mydb[name_table]




def list_of_collection():
	return mydb.list_collection_names()
def show_collection(name_collection):
	mycol = mydb[name_collection]
	liste=[]
	for x in mycol.find():
		print(x)


for i in list_of_collection():
	print('\n')
	print(i)