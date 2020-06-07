# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:36:58 2020

@author: MAlalouf
"""

from GoogleNews import GoogleNews
import pickle

startdate = '02/01/2020'
enddate = '06/07/2020'

# googlenews = GoogleNews(lang="en", start = startdate, end = enddate)
googlenews = GoogleNews()


googlenews.search("trump")
result = googlenews.result()
print(len(result))

print(result[0])

links = [l["link"] for l in result]

with open("testlist.pkl", "wb") as file:
    pickle.dump(result, file)