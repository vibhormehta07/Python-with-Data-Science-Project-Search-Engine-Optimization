#Project in Python
#Search Engine Optimization

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

ip=input("Enter the search keyword:")
resultdict={}
fo=open("url.txt","r+")
fz=fo.read()
urllists=fz.split('\n')
print(urllists)
fo.close()
for url in urllists:
    res=url+ip
    print(res)
    file_handle=urlopen(res)
    html=file_handle.read()
    soup=BeautifulSoup(html,"html.parser")
    for script in soup(["script","style"]):
          script.extract()
    text=soup.get_text().lower()
    List1=[]
    List1.append(text.lower().split())
    i=0
    for x in List1:
        for a in x:
            if ip==a:
                i=i+1
    resultdict.update({res:i})
    
fo=open("results.txt","w")
for d,k in resultdict.items():
    fo.write("%s  "%d)
    fo.write("The no of hits of the keyword is ")
    fo.write("%d \n" %k)

fo.close()




    




