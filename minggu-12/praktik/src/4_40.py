#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[19]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
get_ipython().run_line_magic('timeit', "college.at[cn, 'UGDS_WHITE']")


# In[ ]:




