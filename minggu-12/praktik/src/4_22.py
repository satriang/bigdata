#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[11]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
college.iloc[[60, 99, 3]].index.tolist()


# In[ ]:




