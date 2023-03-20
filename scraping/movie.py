import requests,os
from rich import print
from rich.panel import Panel
from bs4 import BeautifulSoup
from rich.padding import Padding

response=requests.get("https://www.91mobiles.com/hp-laptops-price-list-in-india")
soup=BeautifulSoup(response.text, "html.parser")
nameList=[]
priceList=[]
performance=[]

contain = soup.findAll('div', attrs={"class":"filter-main"})

for i in contain:
    nameList.append(i.find("a").get_text())


rates=soup.findAll('span', attrs={'class':'price price_padding'})

for i in rates:
    priceList.append(i.text)


#  description :

description=soup.findAll('div', attrs={'class':'filter-grey-bar filter_gray_bar_margin grey_bar_custpage'})
lst=[]
for desc in description:
    print(desc.find('div',{'class':'left specs_li'}).find('div').text)

for desc2 in description:
    print(desc2.find('div',{'class':'a filter-list-text'}).find('div').text)

