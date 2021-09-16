# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:56:56 2021

@author: BornaMarkovic
"""
import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title.text

# print the result
print(page_title) 