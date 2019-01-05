#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
sensors = pd.read_csv('data/sensors.csv')
sensors.melt(id_vars=['Group', 'Property'], var_name='Year')        .pivot_table(index=['Group', 'Year'], columns='Property', values='value')        .reset_index()        .rename_axis(None, axis='columns')


# In[ ]:




