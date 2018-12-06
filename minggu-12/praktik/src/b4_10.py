#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
city.loc['Alabama State University':'Reid State Technical College':10]


# In[ ]:




