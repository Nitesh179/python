import requests
from bs4 import BeautifulSoup


res=requests.get('http://www.quotationspage.com/quotes/')

soup=BeautifulSoup(res.content,'html.parser')

authorLink=soup.find('td',{"id":"content"}).find('tr').find_all('a')

authorsName=[]
authorsUrl=[]

for i in authorLink:
    authorsName.append(i.text)
    authorsUrl.append("http://www.quotationspage.com/"+i.get('href'))

for url in authorsUrl:
    response=requests.get(url)   
    soup=BeautifulSoup(response.content,'html.parser')