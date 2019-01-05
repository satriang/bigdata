#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[95]:


crime = pd.read_hdf('data/crime.h5', 'crime')
crime = crime.set_index('REPORTED_DATE')
get_ipython().run_line_magic('timeit', "crime.loc['2015-3-4':'2016-1-1']")


# In[96]:


crime_sort = crime.sort_index()
get_ipython().run_line_magic('timeit', "crime_sort.loc['2015-3-4':'2016-1-1']")


# In[97]:


pd.options.display.max_rows = 60

