#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[145]:


crime = pd.read_hdf('data/crime.h5', 'crime')
criteria = crime['REPORTED_DATE'].dt.year == 2017
round(272 / 365, 3)


# In[ ]:




