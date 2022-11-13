# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 23:05:21 2022

@author: ASUS
"""



import requests
from pyquery import PyQuery as pq


# Function to get download url
def get_download_url(link):
    # Make request to website 
    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    # Get content from post request
    request_content = post_request.content
    str_request_content = str(request_content, 'utf-8')
    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')


    return download_url
    
if __name__ == "__main__":
    
     url = input('Paste the Pinterest URL here :')
   # url = 'https://in.pinterest.com/pin/747316131923974563'
  

print('\nPlease, wait, your file is downloading!')

download_url = get_download_url(url)
import wget
response = wget.download(download_url, "pin.mp4")