#!/usr/bin/env python
# coding: utf-8

# In[1]:



def findindex(dic):
	print("\n\nEnter the KEY to search")
	#key = input()
	key='connect'
	index=dic.get(key)
	return index, key

def getdetails(ind, key,dir2):
	i=0
	string="Key is "+ str(key) +"\nTerm Index is "+ str(ind) + "\n"
	crs = open(dir2+'\doc_index', "r")
	for columns in ( raw.strip().split() for raw in crs ):
#		for i in range(len(columns)):
		if columns[0]==ind:
			string +=  "Number of documents containing term: " + str(columns[2]) + "\n" + "Number of times repeated in corpus: " + str(columns[1])
			print(string)
			return 
	print('Sorry, the desired key is not present')
	return

