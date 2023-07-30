# the Windows users need to navigate to the Python directory, and then install the request module as follows:
# python -m pip install requests

# Install Beautiful package python -m pip install bs4

#*******************************************************************************************************#
# Importing requests package

import requests

# Scarp data from website

requests.get('https://azuredevopslabs.com/')

response = requests.get('https://azuredevopslabs.com/')

print(response)

print (response.url)

print(response.status_code)

#print(response.headers)

#print(response.content)

#******************************************************************************************************#

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text)
# print(soup.prettify()) 