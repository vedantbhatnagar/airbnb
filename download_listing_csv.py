"""
Created on Sat, Mar 6, 2021

@author: Madhur Jajoo
"""

# Import required libraries
import urllib.request
import re
import sys
from bs4 import BeautifulSoup

geo_info_list = []
for geo_info in soup.find_all('h2'):
    print(geo_info.string)
    
# Checks whether URL exists
def is_url_alive(url):
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False
 
def download_airbnb_files(soup_obj, file_type):
    for link in soup_obj.find_all('a'):    
        match = re.search(f'(\w+)/(\d{4}-\d{2}-\d{2})/data/{file_type}', str(link.get('href')))
        if match:
            city_name = match.group(1)
            date = match.group(2)
            if is_url_alive(link.get('href')):
                urllib.request.urlretrieve(link.get('href'),f'F:/Data Science/airbnb/data/{city_name}_{date}_{file_type}) 
                                           
url = "http://insideairbnb.com/get-the-data.html"

#Open URL
page = urllib.request.urlopen(url)

# Create soup instance using scrapped HTML page
soup = BeautifulSoup(page.read(), 'html.parser')

file_type = 'listings.csv.gz'

download_airbbnb_files(soup, file_type):