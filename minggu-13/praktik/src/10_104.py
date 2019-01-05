#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[135]:


crime_sort = pd.read_hdf('data/crime.h5', 'crime')                .set_index('REPORTED_DATE')                .sort_index()
crime_begin = crime_quarterly.iloc[0]
crime_quarterly.div(crime_begin)                .sub(1)                .round(2)                .plot(**plot_kwargs)


# In[ ]:




