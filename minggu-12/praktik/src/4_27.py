#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college.iloc[[100, 200], [7, 15]]


# In[ ]:




