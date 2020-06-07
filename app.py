# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:36:58 2020

@author: MAlalouf
"""

from GoogleNews import GoogleNews

startdate = '02/01/2020'
enddate = '06/07/2020'

googlenews = GoogleNews(lang="en", start = startdate, end = enddate)


test = googlenews.search("police")