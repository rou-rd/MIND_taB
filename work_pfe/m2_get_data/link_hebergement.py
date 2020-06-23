import requests
from bs4 import BeautifulSoup
import re
import database_mango as db
import search as ss



def check_data_duplicate(list_data,t):
	x=False
	for i in list_data:
		if t["name_of_url"]==i["name_of_url"]:	
			x=True
	return x




def get_right_url():
	list_site=ss.search_google("Hébergement Web tunisie")
	list_name=ss.get_name(list_site)
	datas=ss.get_data(list_site,list_name)
	list_of_urls=[]
	for xx in datas:
		try:
			getpage= requests.get(xx["url"])
			getpage_soup= BeautifulSoup(getpage.text, 'html.parser')
			bool2=False
			for link in getpage_soup.findAll('a'):
			        x=link.get('href')
			        bool2="domain" in x
			        if(bool2==True):
			        	doc={"name_of_url":xx["name"],"the_right_url":link.get('href')}
			        	if (check_data_duplicate(list_of_urls,doc)==False):
			        		list_of_urls.append(doc)
			        		print("---------------------------------------------------------"+xx["name"]+"----------------------------------------------------------------------")
		except:			
			pass
	return list_of_urls
list_of_urls=get_right_url()
for x in list_of_urls:
	print(x)



