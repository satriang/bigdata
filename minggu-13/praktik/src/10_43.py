#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[74]:


date = datetime.date(year=2013, month=6, day=7)
date_string_list = ['Sep 30 1984'] * 10000


# In[75]:


get_ipython().run_line_magic('timeit', "pd.to_datetime(date_string_list, format='%b %d %Y')")


# In[76]:


get_ipython().run_line_magic('timeit', 'pd.to_datetime(date_string_list)')


# In[ ]:




