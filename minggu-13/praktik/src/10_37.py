#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[70]:


date = datetime.date(year=2013, month=6, day=7)
ts = pd.Timestamp('2016-10-1 4:23:23.9')
td = pd.Timedelta(125.8723, unit='h')
td


# In[ ]:




