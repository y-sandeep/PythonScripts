# coding: utf-8

import requests 
import time
from bs4 import BeautifulSoup

filename = "jokes.json"	

for i in range(1,12):
	url="http://123hindijokes.com/very-funny-jokes/"+str(i)
	source=requests.get(url)

	source=BeautifulSoup(source.content,"lxml")

	containers = source.find_all('ul',{'class':'statusList'})
	f = open(filename,"a")
	for container in containers:
		jokes=container.find_all("li")
		for joke in jokes:
			j=str(joke).replace('<li>','')
			j=str(j).replace('</li>','')
			j=str(j).replace('<br/>','')
			j=str(j).replace('<p>','')
			j=str(j).replace('</p>','')
			f.write(str(j)+'\n'+'\n')

	f.close()
	print "done"
