#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup

from stemming.porter2 import stem
import sys
import re
import os

def removeAll(lst, token):
	while token in lst:
		lst.remove(token)
	return lst


def stemming(pool):
	temp_pool = []
	for doc_tokens in pool:
		temp_doc = []
		for token in doc_tokens:
			token = stem(token)
			temp_doc.append(token)
		temp_pool.append(temp_doc)
	return temp_pool	

def parseHtml(file_dir):
#	try:
	html = open(file_dir, 'r', encoding='utf-8', errors='ignore').read()
#	except:
#		try :
#			html = open(file_dir, 'r', encoding='windows-1252').read()
#		except:
#			try:
#				html = open(file_dir, 'r', encoding='utf-8').read()
#			except:
#				html = open(file_dir, 'r', encoding='latin-1').read()				
		
	soup = BeautifulSoup(html, "html.parser")
		
	for script in soup(["script", "style"]):
		script.extract()

	text = soup.get_text()
	text = text.encode('utf-8', 'replace')
	text = text.decode('utf-8')
    #THIS CAN BE THE PROBLEM

	text = text.replace('\n', ' ')
	text = text.replace('\\n', ' ')
	text = text.replace('\t', '')
	text = text.replace('\\t', '')
	text = text.replace('\xa0', '')
	text = text.replace('\\xa0', '')
	text = text.replace('\'', '')
	text = text.replace('\\\'', '')

	return text


def removeStopList(pool):
	pool = removeEmptySpace(pool)

	file = open ("stoplist.txt","r")
	content = file.readlines()

	temp_content = []

	for word in content:
		word = word[:-1]
		temp_content.append(word)
	stop_list = temp_content
    

	temp_pool = []
	for doc_tokens in pool:
		 for word in stop_list:
		 	if word in doc_tokens:
		 		removeAll(doc_tokens, word)
		 temp_pool.append(doc_tokens)

	pool = temp_pool 
	return pool
    
def removeEmptySpace(pool):
	return pool
	temp_pool = []
	print("Please Wait, this part takes the longest time")
	for doc_tokens in pool:
		c = ''
		while c in doc_tokens:
			index = doc_tokens.index(c)
			doc_tokens.pop(index)
		temp_pool.append(doc_tokens)
	return temp_pool
	
def getParsedDocs(dir):
	files = getFilesInDir(dir)
	docs = []
	print("Parsing HTML files")
	for file in files:
		text = parseHtml(dir + "\\"+file)
		docs.append(text)
	return docs


def tokenize(docs):

	docs_tokens=[]
	for doc in docs:
		s = re.findall('\w+ (\.?\w+)*',doc)
		docs_tokens.append(s)

	temp_tokens = []
	pool = []
	for i in range(len(docs_tokens)):
		for j in range(len(docs_tokens[i])):
			docs_tokens[i][j] = docs_tokens[i][j].lower()
            
#	for doc_tokens in docs_tokens:
#		for token in doc_tokens:
#			token = token.lower()
#			temp_tokens.append(token)
#		pool.append(temp_tokens)
#	docs_tokens = token
	return docs_tokens

def getFilesInDir(dir):
	lst = []
	for file in os.listdir(dir):
		if file.endswith('.txt'):
			continue
		lst.append(file)
	return lst
    
def tokenizeFile(dir):
	file_dict = assignId(dir)
	file_names = getFilesInDir(dir)
	file = open('docids', 'w', encoding='utf-8', errors='ignore')

	i = 0
	print("Tokenizing File")
	for name in file_names:
		file.write(name+'\t'+ str(file_dict[i][name]) + "\n")
		i += 1
        
def assignId(dir):
	file_names = getFilesInDir(dir)
	file_dict = []
	i = 1
	print("Assigning Doc_ID")
	for file in file_names:
		i += 1
		file_dict.append({file : i})
	return file_dict
    
    
def removeDuplicates(pool):
	temp_pool = []
	print("Removing duplicates ")
	for doc in pool:
		temp_pool.append(list(set(doc)))
	return temp_pool

def assignTermid(pool):
	file = open('termidss','w', encoding='utf-8', errors='ignore')
	i = 0
	print("Assigning Termi ID")
	for docs in pool:
		for token in range(len(docs)): 
			docs[token]=docs[token].encode('utf-8')
			file.write(str(i) + '\t' +docs[token] + "\n")
#			except:
#				try :
#					file.close()
#					file = open('termidss', 'w', encoding='windows-1252')
#					file.write(str(i) + '\t' + token + "\n)
#					file.close()
#					file = open('termidss','w', encoding='utf8', errors='ignore')
#				except:
#					try:
#						file.close()
#						file = open('termidss', 'w', encoding='utf-8')
#						file.write(str(i) + '\t' + token + "\n)
#						file.close()
#						file = open('termidss','w', encoding='utf8', errors='ignore')
#					except:               
#						file.close()
#						file = open('termidss', 'w', encoding='latin-1')
#						file.write(str(i) + '\t' + token + "\n)
#						file.close()
#						file = open('termidss','w', encoding='utf8', errors='ignore')
			i += 1
            
def findIndices(token, lst):
	indices = []
	if token in lst:
		for idx, elem in enumerate(lst):
		    if elem==token:
		        indices.append(idx)
#	print(indices)                
	return indices

