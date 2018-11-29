#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[20]:


college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)
col2.select_dtypes(include=['object']).nunique()


# In[ ]:





# In[ ]:




