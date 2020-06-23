import datetime
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")



def search_google(keywords):
	list_site=[]
	""" create liste of the search from the google with keywords"""
	for site in search(keywords, tld="com", num=10, stop=30, pause=2):
		list_site.append(site)
	return list_site


def get_name(list_site):
	list_name=[]
	for site in list_site:	
		www="www" in site
		host="https://host" in site
		tn="https://tn" in site
		http="http://" in site
		host1="http://host" in site
		tn1="http://tn" in site
		blog="http://blog" in site
		mind="https://mind.hosting" in site
		if((tn==True)and(www==False)and(host==False)and(host1==False)and(tn1==False)and(http==False)and(blog==False)and(mind==False)):
			name_site=site.split('.')[1]
			list_name.append(name_site)
		elif((host==True)and(www==False)and(tn==False)and(host1==False)and(tn1==False)and(http==False)and(blog==False)and(mind==False)):
			name_site=site.split('.')[1]
			list_name.append(name_site)
		elif((www==False)and(host==False)and(tn==False)and(host1==False)and(tn1==False)and(http==False)and(blog==False)and(mind==False)):
			name_site=site.split('.')[0]
			lenth=len(name_site)
			name_site=name_site[8:lenth]
			list_name.append(name_site)
		elif((www==False)and(host==False)and(tn==False)and(host1==True)and(tn1==False)and(http==False)and(blog==False)and(mind==False)):
			name_site=site.split('.')[0]
			lenth=len(name_site)
			name_site=name_site[7:lenth]
			list_name.append(name_site)
		elif((www==False)and(host==False)and(tn==False)and(host1==False)and(tn1==True)and(http==False)and(blog==False)and(mind==False)):
			name_site=site.split('.')[0]
			lenth=len(name_site)
			name_site=name_site[7:lenth]
			list_name.append(name_site)
		elif((www==False)and(host==False)and(tn==False)and(host1==False)and(tn1==False)and(http==True)and(blog==False)and(mind==False)):
			name_site=site.split('.')[0]
			lenth=len(name_site)
			name_site=name_site[7:lenth]
			list_name.append(name_site)
		elif((www==False)and(host==False)and(tn==False)and(host1==False)and(tn1==False)and(http==False)and(blog==True)and(mind==False)):
			name_site=site.split('.')[1]
			list_name.append(name_site)
		elif((www==False)and(host==False)and(tn==False)and(host1==False)and(tn1==False)and(http==False)and(blog==False)and(mind==True)):
			name_site=site.split('.')[0]
			lenth=len(name_site)
			name_site=name_site[8:lenth]
			name_sitex=site.split('.')[1]
			name_sitex=name_sitex[:7]
			list_name.append(name_site+"."+name_sitex)
		else:
			name_site=site.split('.')[1]
			list_name.append(name_site)
	return list_name





def check_data_duplicate(list_data,t):
	x=False
	for i in list_data:
		if t['name']==i['name']:	
			x=True
	return x

def check_data_socialnetwork(t):
	x=False
	i=t
	if(("facebook"==i['name'])or("instagram"==i['name'])or("twitter"==i['name'])or("linkedin"==i['name'])):	
		x=True
	return x



def get_data(list_site,list_name):
	id1=1
	collection=[]
	date=datetime.datetime.today()
	for j,i in zip(list_site,list_name):
		doc={"id":id1+1,"name":i,"url":j,"date":date}
		if(check_data_duplicate(collection,doc)==False):
			if(check_data_socialnetwork(doc)==False):
				collection.append(doc)
	return collection
		
	


list_site=search_google("Hébergement Web tunisie")
list_name=get_name(list_site)
datas=get_data(list_site,list_name)
x=0
for xx in datas:
	x=x+1
	print(xx["name"])
	print(xx["url"])
print(x)












