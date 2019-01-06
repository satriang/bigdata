#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[32]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
start = 'Mesa Community College'
stop = 'Spokane Community College'
college[start:stop:1500]


# In[ ]:




