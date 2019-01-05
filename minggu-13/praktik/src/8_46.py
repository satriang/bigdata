#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[23]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
flights = pd.read_csv('data/flights.csv')
flights.groupby(['AIRLINE', 'MONTH', 'ORG_AIR', 'CANCELLED'])['DEP_DELAY', 'DIST']        .agg(['mean', 'sum'])        .unstack(['ORG_AIR', 'CANCELLED'], fill_value=0)        .swaplevel(0, 1, axis='columns')        .head()


# In[ ]:




