#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[17]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
flights = pd.read_csv('data/flights.csv')
fp = flights.pivot_table(index='AIRLINE', 
                         columns='ORG_AIR', 
                         values='CANCELLED', 
                         aggfunc='sum',
                         fill_value=0).round(2)
fp.head()


# In[ ]:




