#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[126]:


crime = pd.read_hdf('data/crime.h5', 'crime')
weekly_crimes_gby2 = crime.groupby(pd.Grouper(key='REPORTED_DATE', freq='W')).size()
weekly_crimes.plot(figsize=(16,4), title='All Denver Crimes')


# In[ ]:




