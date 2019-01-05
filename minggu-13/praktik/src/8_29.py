#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college2 = pd.read_csv('data/college.csv', 
                      usecols=usecol_func)
college_melted = college2.melt(id_vars='INSTNM', 
                               var_name='Race',
                               value_name='Percentage')
college_melted.head()


# In[ ]:




