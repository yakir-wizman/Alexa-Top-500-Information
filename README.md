# Alexa-Top-500-Information
Short python code for Alexa that take the 500 top websites by country and performs some subdomain and port scanning.

At the beginning I needed a short code that will take all the 500 top websites (By specific country) and will store them as a text file.

Later, I decided to change the code porpuse and to take it to another place.

The code is crawling the 500 top websites from Alexa by given country, and after that will create directory for any website he found and will perform two scanning actions:

1. Scan the 1000 most common ports, that includes http-enum scripts to be run.

2. Scan 1000 most common subdomain name for given address.

Atfer each action the results will be saved at the folder under the name of the domain.

for example, google.com/dnscan.txt & google.com/nmap.txt


You can freely improve the code by adding another features / scanning methods.

Please, do not use this code for illegal propose.

The owner of this code is not responsible for any illegal activity and the usage i by the user responsability.
