#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[9]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
college.iloc[99:102]


# In[ ]:




