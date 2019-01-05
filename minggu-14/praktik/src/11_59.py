#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[268]:


flights = pd.read_csv('data/flights.csv')
flights.groupby('DEST_AIR')['DIST']        .agg(['mean', 'count'])        .query('count > 100')        .sort_values('mean')        .tail(10)        .plot(kind='bar', y='mean', legend=False, 
             rot=0, figsize=(14,4),
             title='Average Distance per Destination')


# In[ ]:




