#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[9]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college2 = pd.read_csv('data/college.csv', 
                      usecols=usecol_func)
melted_inv = college_melted.pivot(index='INSTNM',
                                  columns='Race',
                                  values='Percentage')
college2_replication = melted_inv.loc[college2['INSTNM'], 
                                      college2.columns[1:]]\
                                         .reset_index()
college.T


# In[ ]:




