#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def usingdict(pool):
	dic={}
	i = 0
	print("Assigning Term IDs in a dictionary")
	for docs in pool:
		for token in docs: 
			dic.update({str(token):str(i)})
			i += 1
	return dic

def savePositions2(token_pool, doc_pool):
	file = open('doc_index','w')
	m=0
	for i in range(len(token_pool)):
		for l in range(len(token_pool[i])):
			posno=[]
			docno=[]
			for j in range(len(doc_pool)):
				for k in range(len(doc_pool[j])):
					if token_pool[i][l] in doc_pool[j][k]:
						docno.append(j)
						posno.append(k)
			setofno=list(set(docno))
			m=m+1
			string = str((m)) + ' ' + str(len(docno)) + ' '+ str(len(setofno))
			lendocno=len(docno)
			for j in range(lendocno):
				string += ' ' + str(docno[j]+1) + ',' + str(posno[j]+1)
			string+='\n'
			file.write(string)
	file.close()            
            
def DelsavePositions2(token_pool, doc_pool):
	file = open('Hash_doc_index','w')
	m=0
	for i in range(len(token_pool)):
		for l in range(len(token_pool[i])):
			posno=[]
			docno=[]
			for j in range(len(doc_pool)):
				for k in range(len(doc_pool[j])):
					if token_pool[i][l] in doc_pool[j][k]:
						docno.append(j+1)
						posno.append(k+1)
			setofno=list(set(docno))
			m=m+1
			string = str((m)) + ' ' + str(len(docno)) + ' '+ str(len(setofno))
			lendocno=len(docno)
			p=0
			for j in range(lendocno):
				p=p+1
				if p==1:        
					string += ' ' + str(docno[j]) + ',' + str(posno[j])
				elif docno[j]-docno[j-1] == 0:
					string += ' ' + str(docno[j]-docno[j-1]) + ',' + str(posno[j]-posno[j-1])
				else:
					string += ' ' + str(docno[j]-docno[j-1]) + ',' + str(posno[j])                   
			string+='\n'
			file.write(string)
	file.close()

