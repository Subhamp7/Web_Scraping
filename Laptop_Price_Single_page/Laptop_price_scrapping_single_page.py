# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:09:51 2020

@author: subham
"""
try:
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup as soup
except Exception as e:
    print('Unable to import the Libraries :',e)
    
laptop_list = []
price_list  = []

#accessing the URL
URL="https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&p%5B%5D=facets.price_range.from%3D40000&sort=price_asc&p%5B%5D=facets.price_range.to%3D50000&pageUID=1591708574506&otracker=clp_metro_expandable_4_30.metroExpandable.METRO_EXPANDABLE_laptops-store_WS71EHU11XJS_wp25&fm=neo%2Fmerchandising&iid=M_583bd99e-e26d-411c-92b6-f4feba5879a4_30.WS71EHU11XJS&ppt=clp&ppn=laptops-store&ssid=jqr5cg1qlc0000001593531101890"
page=requests.get(URL)

#True if we have access to the given page
print(page.status_code == 200)
print(type(page))

#parse the page
soup = soup(page.text, "html.parser")
print(type(soup))

#to print the tittle of the page
print((soup.select('title'))[0].get_text())

#class="_3wU53n"
for index in soup.select('._3wU53n'):
    laptop_list.append(index.get_text())
    
#class="_1vC4OE _2rQ-NK"
for index in soup.select('._1vC4OE._2rQ-NK'):
    price_list.append(index.get_text())

#creating dictionary
dict={"Laptop Name" : laptop_list, "Price" : price_list}

#converting the dictionary to a Dataframe
if(len(laptop_list)== len(price_list)):
    final_dataset=pd.DataFrame(dict)
    final_dataset.to_csv('laptop_Price.csv')
else:
    print("Difference in Data")

print('Completed')