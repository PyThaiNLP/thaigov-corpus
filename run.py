# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import codecs
import re
i=15659+1
i2=1
data={}
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
while i<=15753:
	url="http://www.thaigov.go.th/news/contents/details/"+str(i)
	try:
		r = requests.get(url, headers=headers, timeout=60)
		print(i)
		if r.status_code == 200:
			title = re.search('<title>(.*?)</title>',r.text).group(1) #soup.title.text
			if title!="รัฐบาลไทย-ข่าวทำเนียบรัฐบาล-":
				soup = BeautifulSoup(r.text, "lxml")
				article = soup.find('div',{'class':'border-normal clearfix'}).text #soup.article.text
				collection = soup.find('span',{'class':'Circular headtitle-2 font_level6 color2 col-xs-9 remove-xs'}).text

				_text = ''
				for line in article.split('\n'):
					line = line.strip()
					if line:
						_text = _text + '\n' + line
				article = _text
				
				all = title + "\n\n" + article + "\n\nที่มา : " + url
				
				if collection not in data:
					data[collection] = 1
				with codecs.open(collection+"_"+str(data[collection])+".txt", "w", "utf-8-sig") as temp:
					temp.write(all)
				temp.close()
				data[collection] += 1
				print("ok")
				i2+=1
		i+=1
	except:
		print("error")
