#!/usr/bin/env python3

# Modules
import requests
from bs4 import BeautifulSoup

# Variables designed to accept a user's input and store the URL in the "userinput" variable which is then passed to requests.
userinput = input("[Enter the URL]: ")
response = requests.get(userinput)


# Saving a GET request with "requests" into the variable "content" and only accepting successful 200 status codes.:
def content():
    if response.status_code == 200:
        content = response.content
        print("Successful [200] response")
        return content
    else:
        print("Error: ", (response.status_code))

# beautiful soup then parses the data from the "content" variable and extracts the URLs found within the response.

def soup(content):
    soup = BeautifulSoup(content, 'html.parser')

    for link in soup.find_all('a'):
        print(link.get('href'))

    # Call the functions
content_data = content()
if content_data:
    soup(content_data)