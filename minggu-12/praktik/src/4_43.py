#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[21]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')
get_ipython().run_line_magic('timeit', 'college.iloc[row_num, col_num]')


# In[ ]:




