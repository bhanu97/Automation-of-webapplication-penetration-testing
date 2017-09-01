import mechanize
import webbrowser
import urllib2
from bs4 import BeautifulSoup 
m = True
url =raw_input("Enter the url: ")
p = urllib2.urlopen(url)
p= p.read()
s = BeautifulSoup(p,'html.parser')
#print s
for l in s.find_all("meta"):
     if l.get("name")=="generator":
        print l.get("content")
        m =False

if m:
  print "Cannot find the CMS :("


   

