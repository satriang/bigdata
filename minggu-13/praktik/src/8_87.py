#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
sensors = pd.read_csv('data/sensors.csv')
sensors.set_index(['Group', 'Property'])        .stack()        .unstack('Property')        .rename_axis(['Group', 'Year'], axis='index')        .rename_axis(None, axis='columns')        .reset_index()


# In[ ]:




