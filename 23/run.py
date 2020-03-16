# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
firefoxPath="/home/satit/geckodriver"
import codecs
import re
i=15753+1
i2=1
data={}
headers = {'User-Agent': 'Mozilla/5.0 (iPod; CPU iPhone OS 12_0 like macOS) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/12.0 Mobile/14A5335d Safari/602.1.50'}
c=webdriver.Firefox(executable_path=firefoxPath)
#c.implicitly_wait(30)
while i<=19421+5:
	url="https://www.thaigov.go.th/news/contents/details/"+str(i)
	try:
		c.get(url)
		print(i)
		if 200 == 200:
			soup=BeautifulSoup(c.page_source, 'lxml')
			title = soup.find('title').text
			if title!="รัฐบาลไทย-ข่าวทำเนียบรัฐบาล-":
				article = soup.find('div',{'class':'border-normal clearfix'}).text #soup.article.text /html/body/div[4]/div/div/div/div/div/div[1]/div[2]
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
	except Exception as e:
		print(e)
		print("error")
	i+=1
