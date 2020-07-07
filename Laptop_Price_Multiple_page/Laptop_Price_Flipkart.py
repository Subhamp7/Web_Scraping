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

for index in range(0,21,1):
    URL="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=d8f26e3e-b8b0-4e24-9393-1da5b6b25d49&as-searchtext=lap&page=" +str(count)
    page=get(URL)
    print("Connected {} : {} ".format(count,page.status_code==200))
    soup=BeautifulSoup(page.text, 'html.parser')
    count+=1
    
    #class="_3wU53n"
    for index in soup.select('._3wU53n'):
        names.append(index.get_text())
        
    #class="_1vC4OE _2rQ-NK"
    for index in soup.select('._1vC4OE._2rQ-NK'):
        price.append(index.get_text())

#creating dictionary
dict={"Laptop Name" : names, "Price" : price}

#converting the dictionary to a Dataframe
if(len(names)== len(price)):
    final_dataset=pd.DataFrame(dict)
else:
    print("Difference in Data")

final_dataset['Price']=final_dataset['Price'].str.replace(",","").str.extract('(\d+)').astype(int)

#final_dataset.to_csv('laptop_Price.csv')

print('Completed')

    