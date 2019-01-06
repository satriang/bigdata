#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[25]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
state = college['STABBR']
state.iat[1000]


# In[ ]:




