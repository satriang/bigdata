#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[31]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
college.index[4001]


# In[ ]:




