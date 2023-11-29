#!/usr/bin/env python3

# Modules
import requests
from bs4 import BeautifulSoup

# Variables
url = 'https://google.com'
response = requests.get(url)


# Saving a GET request with "requests" into the variable "content":
if response.status_code == 200:
    content = response.content
    print("Successful [200] response")
    
else:
    print("Error: {response.status_code}")

soup = BeautifulSoup(content, 'html.parser')

for link in soup.find_all('a'):
        print(link.get('href'))
