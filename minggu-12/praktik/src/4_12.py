#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
city.loc['Reid State Technical College':'Alabama State University':10]


# In[ ]:




