#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[6]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
city.loc['Heritage Christian University']


# In[ ]:




