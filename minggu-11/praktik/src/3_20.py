#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[4]:


college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
new_mem = col2.memory_usage(deep=True)
new_mem


# In[ ]:




