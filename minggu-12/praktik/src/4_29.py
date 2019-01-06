#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college.iloc[5, -4]


# In[ ]:




