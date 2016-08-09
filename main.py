import os
import re
import requests
import subprocess

alexa_url   = "http://www.alexa.com/topsites/countries;0/US"
request     = requests.get(alexa_url).text
matches     = re.search(r'<b>(\d+)<\/b> of <b>(\d+)<\/b>', request)
pages       = int(matches.group(2)) / int(matches.group(1))
domains     = ['.com', '.net'] # Filter for some domains
for i in range(pages):
    alexa_page      = "http://www.alexa.com/topsites/countries;%i/US" % i
    request_page    = requests.get(alexa_page).text
    urls            = re.findall(r'<a href="\/siteinfo\/(.*)">', request_page)
    for x in urls:
        if any(domain in x for domain in domains):
            if not os.path.exists(x):
                os.makedirs(x)
            subprocess.call("python dnscan.py -d " +x+ " -t 10 -w subdomains.txt -o " +x+ "/dnscan.txt", shell=True) # If you have feeling that subprocess.call is slow, use subprocess.popen
            subprocess.call("nmap -top-ports 1000 -Pn -sV -oN " +x+ "/nmap.txt --script=http-enum " +x, shell=True) # Same thing as here.
