#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[163]:


crime_sort = pd.read_hdf('data/crime.h5', 'crime')                .set_index('REPORTED_DATE')                .sort_index()
common_attrs = set(dir(crime_sort.index)) & set(dir(pd.Timestamp))
crime_sort.index.weekday_name.value_counts()


# In[ ]:




