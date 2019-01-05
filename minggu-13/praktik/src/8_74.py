#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[54]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
inspections = pd.read_csv('data/restaurant_inspections.csv', parse_dates=['Date'])
inspections.pivot_table(index=['Name', 'Date'], 
                        columns='Info', 
                        values='Value', 
                        aggfunc='first') \
           .reset_index()\
           .rename_axis(None, axis='columns')


# In[ ]:




