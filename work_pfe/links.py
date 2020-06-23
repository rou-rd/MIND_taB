import requests
from bs4 import BeautifulSoup
import re
import psycopg2

conn = psycopg2.connect(host="localhost",database="myproject", user="root", password="toor")
cur = conn.cursor()

cur.execute("""SELECT * FROM concurrents""")
rows = cur.fetchall()
for row in rows:
    getpage= requests.get(row[2])
    print(row[2])
    getpage_soup= BeautifulSoup(getpage.text, 'html.parser')
    bool=False
    bool2=False
    for link in getpage_soup.findAll('a', attrs={'href': re.compile("^https://")}):
        x=link.get('href')
        bool="cart.php" in x
        bool2="cart/" in x
        if(bool==True)or(bool2==True):
            print("whcms")
