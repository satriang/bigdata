#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
pd.options.display.max_rows = 6
college.loc['University of Alaska Anchorage']


# In[ ]:




