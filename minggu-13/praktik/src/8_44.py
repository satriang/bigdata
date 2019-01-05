#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[20]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
flights = pd.read_csv('data/flights.csv')
fg = flights.groupby(['AIRLINE', 'ORG_AIR'])['CANCELLED'].sum()
fg_unstack = fg.unstack('ORG_AIR', fill_value=0)
fp.equals(fg_unstack)


# In[ ]:




