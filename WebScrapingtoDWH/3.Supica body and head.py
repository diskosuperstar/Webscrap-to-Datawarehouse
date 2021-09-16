# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:02:47 2021

@author: BornaMarkovic
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text

page_body = soup.body

page_head = soup.head

print(page_body)

