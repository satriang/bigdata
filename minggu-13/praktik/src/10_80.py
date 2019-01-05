#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[114]:


crime = pd.read_hdf('data/crime.h5', 'crime').set_index('REPORTED_DATE')
dt = pd.Timestamp('2012-1-16 13:40')
dt + pd.DateOffset(months=1)


# In[ ]:




