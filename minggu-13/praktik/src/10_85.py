#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[117]:


crime_sort = pd.read_hdf('data/crime.h5', 'crime')                .set_index('REPORTED_DATE')                .sort_index()
weekly_crimes = crime_sort.resample('W').size()
weekly_crimes.head()


# In[ ]:




