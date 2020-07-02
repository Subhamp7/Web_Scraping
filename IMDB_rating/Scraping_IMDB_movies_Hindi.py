# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:39:07 2020

@author: subham
"""
try:
    from requests import get
    import numpy as np
    import pandas as pd
    from bs4 import BeautifulSoup
    
except Exception as e:
    print("Importing libraries was unsuccessful",e)
''' 
https://www.imdb.com/list/ls045285923/
https://www.imdb.com/list/ls045285923/?sort=list_order,asc&st_dt=&mode=detail&page=2
'''

titles       = []
years        = []
imdb_ratings = []
votes        = []
count        = 0

list_of_page=["https://www.imdb.com/list/ls045285923/",
"https://www.imdb.com/list/ls045285923/?sort=list_order,asc&st_dt=&mode=detail&page=2"]

for index in list_of_page:
    
    URL="https://www.imdb.com/list/ls045285923/"
    page=get(URL)
    print("Connected {} : {} ".format(count,page.status_code==200))
    soup=BeautifulSoup(page.text, 'html.parser')
    movies=soup.find_all('div',class_="lister-item mode-detail")
    count+=1
    for index in movies:
        title=index.h3.a.text
        titles.append(title)
        
        year=index.h3.find('span', class_="lister-item-year text-muted unbold").text
        years.append(year)
        
        rating=index.find('span', class_="ipl-rating-star__rating").text
        imdb_ratings.append(rating)
        
        vote=index.find_all('span', attrs ={"name" : "nv"})
        vote=vote[0].text
        votes.append(vote)

dict={"Titles" : titles, "Year" : years, "IMDB Ratings": imdb_ratings, "Votes": votes}

final_dataset=pd.DataFrame(dict)

final_dataset["Year"]                   = final_dataset["Year"].str.extract('(\d+)').astype(int)
final_dataset["IMDB Ratings"]           = final_dataset["IMDB Ratings"].astype(float)
final_dataset["Votes"]                  = final_dataset["Votes"].str.replace(",","").astype(int)
final_dataset["Percentage of Votes"]    = (final_dataset["Votes"]/final_dataset["Votes"].sum())*1000

#to convert dataframe to csv
#final_dataset.to_csv("IMDB_movies_list")
