#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[12]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
employee = pd.read_csv('data/employee.csv')
agg = employee.groupby(['RACE', 'GENDER'])['BASE_SALARY'].mean().astype(int)
agg.unstack('GENDER')


# In[ ]:




