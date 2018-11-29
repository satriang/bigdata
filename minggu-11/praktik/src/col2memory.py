#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[17]:


college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
original_mem = col2.memory_usage(deep=True)
original_mem


# In[ ]:





# In[ ]:




