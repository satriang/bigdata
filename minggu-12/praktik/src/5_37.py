#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[77]:


college = pd.read_csv('data/college.csv')
college2 = college.set_index('STABBR')
college3 = college2.sort_index()
college_unique = college.set_index('INSTNM')
get_ipython().run_line_magic('timeit', "college_unique.loc['Stanford University']")


# In[ ]:




