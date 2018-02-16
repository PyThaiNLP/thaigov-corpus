# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import codecs
import re
i=10103
i2=1
data={}
while i<=10151:
	url="http://www.thaigov.go.th/news/contents/details/"+str(i)
	try:
		r = requests.get(url)
		print(i)
		if(r.status_code==200):
			title = re.search('<title>(.*?)</title>',r.text).group(1) #soup.title.text
			if title!="รัฐบาลไทย-ข่าวทำเนียบรัฐบาล-":
				soup = BeautifulSoup(r.text, "lxml")
				article = soup.find('div',{'class':'border-normal clearfix'}).text #soup.article.text
				collection=soup.find('span',{'class':'Circular headtitle-2 font_level6 color2 col-xs-9 remove-xs'}).text
				all=title+"\n\n"+article+"\n\nที่มา : "+url
				if collection not in data:
					data[collection]=1
				with codecs.open(collection+"_"+str(data[collection])+".txt", "w", "utf-8-sig") as temp:
					temp.write(all)
				temp.close()
				data[collection]+=1
				print("ok")
				i2+=1
		i+=1
	except:
		print("error")
