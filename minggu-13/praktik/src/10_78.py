#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[112]:


crime = pd.read_hdf('data/crime.h5', 'crime').set_index('REPORTED_DATE')
first_date = crime_sort.index[0]
first_date + pd.offsets.MonthBegin(6)


# In[ ]:




