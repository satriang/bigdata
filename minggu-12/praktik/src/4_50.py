#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[26]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college[10:20:2]


# In[ ]:




