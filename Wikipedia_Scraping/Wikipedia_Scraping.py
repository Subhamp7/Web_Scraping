# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 23:07:37 2020

@author: subham
"""

#loading the dataset
try:
    import nltk
    import urllib
    import re
    from bs4 import BeautifulSoup
    from nltk.corpus import stopwords
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    nltk.download('stopwords')
    nltk.download('punkt')
    
except Exception as e:
    print('Unable to load the Libraries',e)
    
#getting data from wiki
page=urllib.request.urlopen("https://en.wikipedia.org/wiki/Machine_learning").read()
soup=BeautifulSoup(page,"lxml")

#adding all the sentences with P tag in temp
temp=""
for index in soup.find_all('p'):
    temp+=index.text
    
#processing the temp
temp=re.sub(r'\[[0-9]*\]',' ',temp)#removing the number tags[11]
temp=re.sub(r'\s+',' ',temp)#removing the space
temp = temp.lower()#changing all the words to lower case
temp = re.sub(r'\d',' ',temp)#removing individual digits

#plotting a wordcloud
cloud=WordCloud().generate(temp)
plt.imshow(cloud)

# Preparing the dataset
sentences = nltk.sent_tokenize(temp)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

