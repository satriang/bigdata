#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[146]:


crime = pd.read_hdf('data/crime.h5', 'crime')
crime_pct = crime['REPORTED_DATE'].dt.dayofyear.le(272)                                   .groupby(year)                                   .mean()                                   .round(3)
crime_pct


# In[ ]:




