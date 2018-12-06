#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[7]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
labels


# In[ ]:




