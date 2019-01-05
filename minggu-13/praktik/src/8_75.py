#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[55]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
cities = pd.read_csv('data/texas_cities.csv')
cities


# In[ ]:




