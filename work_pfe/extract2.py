import requests
from bs4 import BeautifulSoup
import re
import json
import nltk


def get_data_from_url(url):
	url=url
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


	f = open("oxahost.txt","w+")
	f.write(text)



get_data_from_url()