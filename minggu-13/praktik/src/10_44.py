#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[79]:


crime = pd.read_hdf('data/crime.h5', 'crime')
crime.dtypes


# In[ ]:




