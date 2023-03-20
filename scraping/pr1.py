import requests,os
from rich import print
from rich.panel import Panel
from bs4 import BeautifulSoup
from rich.padding import Padding

response=requests.get("https://top40weekly.com/")
soup=BeautifulSoup(response.text, "html.parser")

# main_contain = soup.findAll('div', attrs={"class":"x-main left"})
# for title in main_contain:
#     print(title.text)
# print(main_contain)
# print(soup.body)  

heading=soup.findAll('h4', attrs={'class':"h-custom-headline cs-ta-left h4"})
for i in heading:
  os.system('clear')
  print(Padding(f"\t\t\t[red]{i.text}",(2,0,2,0)))

mname=soup.findAll('div', attrs={'class':"x-text"})
l=[]
for i in mname:
     l.append(i.text)

l.pop(0)

print(Panel.fit(l[1]))
