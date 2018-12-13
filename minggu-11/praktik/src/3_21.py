#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[22]:


college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
original_mem = col2.memory_usage(deep=True)
col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)
col2['STABBR'] = col2['STABBR'].astype('category')
new_mem = col2.memory_usage(deep=True)
new_mem / original_mem

