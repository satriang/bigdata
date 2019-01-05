#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[115]:


crime = pd.read_hdf('data/crime.h5', 'crime').set_index('REPORTED_DATE')
do = pd.DateOffset(years=2, months=5, days=3, hours=8, seconds=10)
pd.Timestamp('2012-1-22 03:22') + do


# In[ ]:




