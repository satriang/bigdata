#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[142]:


crime = pd.read_hdf('data/crime.h5', 'crime')
wd_counts = crime['REPORTED_DATE'].dt.weekday_name.value_counts()
weekday = crime['REPORTED_DATE'].dt.weekday_name
year = crime['REPORTED_DATE'].dt.year

crime_wd_y = crime.groupby([year, weekday]).size()
crime_wd_y.head(10)


# In[ ]:




