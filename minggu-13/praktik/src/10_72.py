#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[105]:


crime = pd.read_hdf('data/crime.h5', 'crime').set_index('REPORTED_DATE')
crime_sort = crime.sort_index()
pd.options.display.max_rows = 6
crime_sort.first('5D')


# In[ ]:




