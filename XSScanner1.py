import mechanize
import urllib2
import urllib
import string
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib2 import urlopen
from urllib import urlencode
from urlparse import uses_query
import requests
import httplib
import urlparse
import os
import sys


#For [SSL: CERTIFICATE_VERIFY_FAILED] errors
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
#br.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',)]
'''br.addheaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}'''
br.set_handle_refresh(False)

def linkcheck(ur2):
    br.open(ur2)
    for l in br.links():
        print l.url

def paramfind(ur3):
    parsed_url = urlparse.urlparse(ur3)
    #print parsed_url
    parsed_url_list = list(parsed_url)
    #print parsed_url_list   
    return parsed_url_list


ur1 = raw_input("Enter url:")
br.open(ur1)
parsed_url_list1 = paramfind(ur1)
parameters = dict(urlparse.parse_qs(parsed_url_list1[4]))


if parameters =={}:
   print "No parameters in the url.........\n We are finding parameters for u:)" 
   #linkcheck(ur1) 
else:
    list2 = parsed_url_list1;
    print list2
    #print parameters
    
    for i in parameters:
        k =parameters[i]
        print "Checking the "+ i +" parameter:"
        f=open("list1.txt")
        while True:
              r=f.readline()
              if r=="":
                 break
              parameters[i] = r        #changing a single parameter
              parsed_url_list1[4] = urlencode(parameters)
              x= urlparse.urlunparse(parsed_url_list1)
              print x
              res = urllib.urlopen(x)
              res =res.read()
              if r in res:
                 print "Vulnerability found"
              else:
                  print"No vulnerability found"
        parameters[i] =k
        parsed_url_list1 = list2
    
    #o1 = o._replace(i = "alert(1)")
    #path = o.scheme+"://"+o.netloc+o.path
    #print path
    #paramfind(ur1)
   

#print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

'''k=  parse_qs(urlparse(ur).query)
print k
#print parse_qs(urlparse(ur).query, keep_blank_values=True)

f=open("list1.txt")

for i in range(len(k["q"])):
    r=f.readline()
    print r
    new_ur = string.replace(ur,str(k["q"][i]),str(r))
    print new_ur
    res = urlopen(new_ur)
    print "Response when the above payload is injected is: "
    print res 
'''

