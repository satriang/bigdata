#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[26]:


df = pd.read_csv('data/stackme.csv')
df2 = df.rename(columns = {'a1':'group1_a1', 'b2':'group1_b2',
                           'd':'group2_a1', 'e':'group2_b2'})
pd.wide_to_long(df2, 
                stubnames=['group1', 'group2'], 
                i=['State', 'Country', 'Test'], 
                j='Label', 
                suffix='.+', 
                sep='_')


# In[ ]:




