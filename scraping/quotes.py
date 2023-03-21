import html5lib,requests,json
from bs4 import BeautifulSoup
from rich import print
from rich.console import Console
from rich.table import Table

# link work :



res=requests.get('http://www.quotationspage.com/quotes/')

soup=BeautifulSoup(res.content,'html.parser')

authorLink=soup.find('td',{"id":"content"}).find('tr').find_all('a')

authorsName=[]
authorsUrl=[]
quoteList=[]
dic={}
mydata=[]

for i in authorLink:
    authorsName.append(i.text)
    authorsUrl.append(i.get('href'))
    
for url in authorsUrl:

    res=requests.get("http://www.quotationspage.com/"+url)

    soup=BeautifulSoup(res.content,'html.parser')

   
    quotes=soup.find('td',{"id":"content"}).findAll('dt',{"class":"quote"})
    # for i in quotes:
    #     dic['quotes']=i.text
    #     quoteList.append(dic.copy())  
    
    for i,j in zip(quotes,authorsName):
        mydata.append({:i.text})
        dic['quotes']=i.text
        quoteList.append(dic.copy())  
        

    print(mydata)

    #  insert data into json file :

    '''f=open('Qtdata.json','w')
    # json.dump(quoteList,f,indent=4)
    f.close()'''

    #  fetch data from json file :
    f1=open('Qtdata.json','r')
    data=json.load(f1)
    # print(data[0]['quotes'])

 
    # for author in authorsName:

   
    table = Table(title=f"\n\n[bold magenta]Quatations By author \n\n")

    table.add_column("QUOTES LISTS",style="blue_violet",no_wrap=False)

    for i in data:        
            table.add_row(i['quotes'])
            table.add_row('\n')

    console = Console()
    console.print(table)    

    f1.close()