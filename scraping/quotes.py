from rich.console import Console
from rich.table import Table
import html5lib,requests,json
from bs4 import BeautifulSoup
from rich import print
from rich.console import Console
from rich.table import Table
import time,os
from rich.progress import track

res=requests.get('http://www.quotationspage.com/quotes/')

soup=BeautifulSoup(res.content,'html.parser')

authorLink=soup.find('td',{"id":"content"}).find('tr').find_all('a')

authorsName=[]
authorsUrl=[]
quoteList=[]
data=[]

# check file available or not :

fileavailable=os.path.isfile('QuoteData1.json')

if fileavailable:
    # import json data :

    f=open('QuoteData1.json','r')
    data=json.load(f)

# if file Not available execute this :

if len(data)==0:
    for i in authorLink:
        authorsName.append(i.text)
        authorsUrl.append(i.get('href'))

    for url,name,q in zip(authorsUrl,authorsName,track(range(111), description="Scanning Quotes...")):

        res=requests.get("http://www.quotationspage.com/"+url)

        soup=BeautifulSoup(res.content,'html.parser')

        tempQuote=[]
        quotes=soup.find('td',{"id":"content"}).findAll('dt',{"class":"quote"})
        for i in quotes: tempQuote.append(i.text)

        quoteList.append({"Author":name,"Quotes":tempQuote})
        # print({"Author":name,"Quotes":tempQuote})

    # insert data in json file :
   
    f=open('QuoteData1.json','w')
    json.dump(quoteList,f,indent=4)
    f.close()

else :
    author=input("Enter Author Name : ")

    for i in data:
        for j in i:
            if i[j]==author:

                table = Table(title="\n\n [bold magenta]Quotations by Author!!!\n")
                table.add_column(author, style="cyan", no_wrap=False)
                
                for qt in i['Quotes']:
                    table.add_row(str(qt))
                    table.add_row("\n")

                console = Console()
                console.print(table)

