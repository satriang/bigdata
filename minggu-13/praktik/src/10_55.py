#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[89]:


crime = pd.read_hdf('data/crime.h5', 'crime')
crime = crime.set_index('REPORTED_DATE')
pd.options.display.max_rows = 4
crime.loc['2015-3-4':'2016-1-1'].sort_index()


# In[ ]:




