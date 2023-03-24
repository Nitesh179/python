from bs4 import BeautifulSoup
import requests,json,os

response=requests.get("https://www.failory.com/startups/india/")

soup=BeautifulSoup(response.text, "html.parser")

data=soup.find('div',id='content').find('div',class_= None).find_all('article',id='failed-startup-text')

mainList=[]
dict={}
fetchdata=[]

file=os.path.isfile('startups.json')

if file:
    f=open('startups.json','r')
    fetchdata=json.load(f)

    f.close()

if len(fetchdata)==0:
    for alldata in data:

        companyName=alldata.find_all('h3')
        link=alldata.find_all('a')[:-2]
        desc=alldata.find_all('ul')[:-2]

        for i,k,l in zip(companyName,desc,link):
            coStr=str(i.text).split()
            dict={"Company Name":coStr[1],"Intro":i.find_next_sibling("p").text,"Detail":k.text,"URL":l.get('href')}
            mainList.append(dict.copy())  

    
    f1=open('startups.json','w')
    json.dump(mainList,f1,indent=4)  

    f1.close()      
    
else :
    print(fetchdata)  

