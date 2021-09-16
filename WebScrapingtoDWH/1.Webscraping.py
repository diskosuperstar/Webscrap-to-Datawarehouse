# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:36:14 2021

@author: BornaMarkovic
"""

import requests
res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

text = res.text
status = res.status_code

print(text,status)

