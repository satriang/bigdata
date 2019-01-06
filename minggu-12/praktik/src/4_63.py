#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[39]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
college = college.sort_index()
pd.options.display.max_rows = 6
college = college.sort_index(ascending=False)
college.loc['E':'B']


# In[ ]:




