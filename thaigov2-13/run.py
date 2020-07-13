# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import codecs
import re
i=32311+1
i2=1
data={}
import time
num = 0
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-javascript")
browser = webdriver.Chrome(chrome_options=chrome_options)
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
n_ok=0
while True:
	url="https://www.thaigov.go.th/news/contents/details/"+str(i)
	browser.get(url)
	try:
		#r = requests.get(url, headers=headers, timeout=60)
		print(i)
		num=0
		time.sleep(2)
		if True:#r.status_code == 200:
			title = re.search('<title>(.*?)</title>',browser.page_source).group(1) #soup.title.text r.text
			if title!="รัฐบาลไทย-ข่าวทำเนียบรัฐบาล-":
				soup = BeautifulSoup(browser.page_source,"html.parser") #"lxml")
				article = soup.find('div',{'class':'border-normal clearfix'}).text #soup.article.text
				print("a")
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
				n_ok=i
		i+=1
	except Exception as e:
		print("error "+str(e))
		if num>20:
			break
		i+=1
		num+=1
	print("ok " +str(n_ok))
