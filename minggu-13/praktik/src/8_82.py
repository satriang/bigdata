#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[63]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
cities = pd.read_csv('data/texas_cities.csv')
geolocations = cities.Geolocation.str.split(pat='. ', expand=True)
geolocations.columns = ['latitude', 'latitude direction', 'longitude', 'longitude direction']
geolocations = geolocations.astype({'latitude':'float', 'longitude':'float'})
cities_tidy = pd.concat([cities['City'], geolocations], axis='columns')
temp = geolocations.apply(pd.to_numeric, errors='ignore')
cities.Geolocation.str.split(pat='° |, ', expand=True)


# In[ ]:




