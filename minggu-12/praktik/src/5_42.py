#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[83]:


college = pd.read_csv('data/college.csv')
college2 = college.set_index('STABBR')
college3 = college2.sort_index()
college_unique = college.set_index('INSTNM')
college.index = college['CITY'] + ', ' + college['STABBR']


# In[86]:


college[(college['CITY'] == 'Miami') & (college['STABBR'] == 'FL')].equals(college.loc['Miami, FL'])


# In[ ]:




