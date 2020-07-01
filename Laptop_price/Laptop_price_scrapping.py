# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:09:51 2020

@author: subham
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

#requesting data from page
page=requests.get("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&p%5B%5D=facets.price_range.from%3D40000&sort=price_asc&p%5B%5D=facets.price_range.to%3D50000&pageUID=1591708574506&otracker=clp_metro_expandable_4_30.metroExpandable.METRO_EXPANDABLE_laptops-store_WS71EHU11XJS_wp25&fm=neo%2Fmerchandising&iid=M_583bd99e-e26d-411c-92b6-f4feba5879a4_30.WS71EHU11XJS&ppt=clp&ppn=laptops-store&ssid=jqr5cg1qlc0000001593531101890")
soup = BeautifulSoup(page.text, 'html.parser')

dollar_tree_list = soup.find_all('href')
