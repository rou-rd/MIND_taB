import re
import nltk












with open ("oxahost.txt", "r") as myfile:
    data=myfile.read()

"""
sentens=sentences = nltk.tokenize.sent_tokenize(data)

tokens = [nltk.tokenize.word_tokenize(s) for s in sentences]
pos_tagged_tokens = [nltk.pos_tag(t) for t in tokens]
ne_chunks = nltk.batch_ne_chunk(pos_tagged_tokens)
print (ne_chunks)
"""
r3 = re.findall(r"\.[a-z].*",data)
r2 = re.findall(r"\d+\.\d+",data)
r1 = re.findall(r"\d+,\d+",data)
x = re.search(r"^[0-9].*DT|dt",data)
r4 = re.findall(r"\d+\d+",data)
x1 = re.findall(r'[0-9]+[\.|,]?[0-9]*\s?.DT | [0-9]+[\.|,]?[0-9]*\s?.dt',data)

print(r3)
print("---------------------------------------------------------------------------------------------")
print(r2)
print("---------------------------------------------------------------------------------------------")
print(r1)
print("---------------------------------------------------------------------------------------------")
print(x)
print("---------------------------------------------------------------------------------------------")
print(r4)
print("---------------------------------------------------------------------------------------------")
print(x1)



x=[]
for i,n in zip(r2,r3):
	doc={"name_of_domain":i,"price":n}
	x.append(doc)
print(x)