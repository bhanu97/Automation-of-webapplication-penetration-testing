import whois
url = raw_input("Enter the url: ")
d = whois.whois(url)
print "Domain Details: "
print d

#another way but not parsed

'''import pythonwhois
site = raw_input("Enter the url: ")
d = pythonwhois.get_whois(site)
print d
'''
#another way

'''
import subprocess
url =raw_input("enter the site: ")
subprocess.call(["pwhois", url])
'''
