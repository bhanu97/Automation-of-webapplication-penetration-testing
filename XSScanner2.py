import mechanize
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

#For [SSL: CERTIFICATE_VERIFY_FAILED] errors
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_refresh(False)

def ask():
    x = raw_input("Do u want to inject another payload??[y/n]: ") 
    if x=="Y" or x=="y":
       driver.close()
       return True       
    elif x=="N"or x=="n":
         driver.close()
         raise SystemExit
    else:
        print "Invalid option"
        ask()


ur1 = raw_input("Enter  url:")
response=br.open(ur1)
soup=BeautifulSoup(response,'html.parser')
nlfs=[]
nlff=[]

for a in soup.find_all("form"):
    if (a.get("name")!=None):
       nlff.append(str(a.get("name")))
for b in soup.find_all("input"):
    #print b
    if (b.get("name")!=None) and (b.get("type")=="text" or b.get("type")==None)and b.get("name")not in nlff:
	nlfs.append(str(b.get("name")))
for c in soup.find_all("textarea"):
    if (c.get("name")!=None) and (c.get("type")!="hidden")and c.get("name")not in nlff and c.get("name")not in nlfs:
        nlfs.append(str(c.get("name")))

print nlff 
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print nlfs    

for na in nlfs:
    print na
    f=open("list1.txt")
    while True:
          r=f.readline()
          print "Injecting the below payload: "
          print r
          driver = webdriver.Firefox()
          driver.get(ur1)
          time.sleep(10)
          try: 
             element = driver.find_element_by_name(na)
             element.send_keys(r)
             element.submit()
             
          except():
                print"Parameter not tracable" 
          #driver.implicitly_wait(20)
          if ask():
             continue

           


          
             
         

