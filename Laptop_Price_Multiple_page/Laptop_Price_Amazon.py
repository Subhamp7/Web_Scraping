# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:22:04 2020

@author: subham
"""
try:
    from requests import get
    import numpy as np
    import pandas as pd
    from bs4 import BeautifulSoup
    
except Exception as e:
    print("Importing libraries was unsuccessful",e)

names = []
price = []
count = 0

URL="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=d8f26e3e-b8b0-4e24-9393-1da5b6b25d49&as-searchtext=lap&page=1"
page=get(URL)
print("Connected {} : {} ".format(count,page.status_code==200))
soup=BeautifulSoup(page.text, 'html.parser')

laptops=soup.find_all('div',class_="bhgxx2 col-12-12")
count+=1

for index in laptops:
   
    price_1=index.find('div', class_="_1vC4OE _2rQ-NK").text
    price.append(price_1)
    
    

    

