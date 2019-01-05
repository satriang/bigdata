#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[65]:


date = datetime.date(year=2013, month=6, day=7)
td1 = pd.to_timedelta([10, 100], unit='s')
td2 = pd.to_timedelta(['3 hours', '4 hours'])
td1 + td2


# In[ ]:




