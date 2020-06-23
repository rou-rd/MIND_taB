import requests
from bs4 import BeautifulSoup
import re
import json
import nltk
import search as ss


list_site=ss.search_google("Hébergement Web tunisie")
list_name=ss.get_name(list_site)
datas=ss.get_data(list_site,list_name)
for xx in datas:
	try:
		url=xx["url"]
		r= requests.get(url)
		html=r.text
		soup =BeautifulSoup(html, "html.parser") 
		for script in soup(["script", "style"]):
		    script.decompose()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)

		f = open(xx["name"]+".txt","w+")
		f.write(text)
	except:
		pass