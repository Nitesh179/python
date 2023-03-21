import requests,os
from rich import print
from rich.panel import Panel
from bs4 import BeautifulSoup
from rich.padding import Padding
import html5lib
from rich.console import Console
from rich.table import Table

response=requests.get("https://www.91mobiles.com/hp-laptops-price-list-in-india")
htmldata=response.content
soup=BeautifulSoup(htmldata, "html.parser")
nameList=[]
priceList=[]
descList=[]
performList=[]



contain = soup.find_all('div', attrs={"class":"filter-main"})

for i in contain:
    for j in i.find('a').stripped_strings:
     nameList.append(j)


rates=soup.findAll('span', attrs={'class':'price price_padding'})

for i in rates:
    priceList.append(i.text)
   


#  description :

description=soup.find_all('div', attrs={'class':'filter-grey-bar filter_gray_bar_margin grey_bar_custpage'})


for i in description:
    for j in i.find_all('div',{'class':'left specs_li'}):
    #  print(j.next_sibling.text)
       descList.append("==================")
    #    print("=")
       for k in j.stripped_strings:
         descList.append(k)
        #    print(k)


# showing data:

table = Table(title="Scraping data of HP laptops ")

for name in nameList[0]:
    for price in priceList[0]:
       for desc in descList[0]:
         table.add_column(name, justify="right", style="cyan", no_wrap=True)

# table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
# table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)        