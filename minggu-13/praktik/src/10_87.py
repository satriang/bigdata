#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[118]:


crime_sort = pd.read_hdf('data/crime.h5', 'crime')                .set_index('REPORTED_DATE')                .sort_index()
weekly_crimes = crime_sort.resample('W').size()
len(crime_sort.loc[:'2012-1-8'])


# In[119]:


len(crime_sort.loc['2012-1-9':'2012-1-15'])


# In[ ]:




