import requests,os,json
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
    l2=[]
    i.find_all('div',{'class':'left specs_li'})
    for j in i.stripped_strings:
     l2.append(j)
     descList.append(l2)
    
products={}
list=[]

for i,j,k in zip(nameList,priceList,descList):
   products["NameList"]=i
   products['Desc']=k
   products["PriceList"]=j
   list.append(products.copy())

# insert data in json file :

# f=open("data.json",'w')
# json.dump(list,f,indent=4)
# f.close()

#  Showing Data :

f2=open('data.json','r')
data=json.load(f2)

table = Table(title="\n\n[bold magenta]91 Mobiles Website Scrap data \n\n")
for i in data[0]:
    if i=='NameList':
        table.add_column(i, style="blue_violet",no_wrap=False,max_width=20)
    elif i=='Desc'  :  table.add_column(i, style="blue_violet",no_wrap=False,max_width=40) 
    else :  table.add_column(i, style="blue_violet",no_wrap=False)
    

for i in data:
    nm=""
    for j in i:
     nm=i['NameList']
     pr=i['PriceList']
     dc=i['Desc']
     table.add_row(str(nm),str(dc),str(pr))
     table.add_row('\n','\n','\n')

f2.close

console = Console()
console.print(table)        
