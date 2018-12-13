#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[24]:


college = pd.read_csv('data/college.csv')
college.loc[0, 'CURROPER'] = 10000000
college.loc[0, 'INSTNM'] = college.loc[0, 'INSTNM'] + 'a'
# college.loc[1, 'INSTNM'] = college.loc[1, 'INSTNM'] + 'a'
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)


# In[ ]:




