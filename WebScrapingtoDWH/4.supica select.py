# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:16:13 2021

@author: BornaMarkovic
Select all <h1> tags and store them inside of all_h1_tags and then print it.
Also select the seventh <p> tag on the page
"""

import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

all_h1_tags = []
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

seventh_p_text = soup.select('p')[6].text

print(all_h1_tags)
print(seventh_p_text)