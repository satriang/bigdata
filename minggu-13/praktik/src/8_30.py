#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college2 = pd.read_csv('data/college.csv', 
                      usecols=usecol_func)
melted_inv = college_melted.pivot(index='INSTNM',
                                  columns='Race',
                                  values='Percentage')
melted_inv.head()


# In[ ]:




