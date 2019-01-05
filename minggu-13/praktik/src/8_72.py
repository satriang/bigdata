#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[52]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
inspections = pd.read_csv('data/restaurant_inspections.csv', parse_dates=['Date'])
insp_tidy = inspections.set_index(['Name','Date', 'Info'])                                .unstack('Info')                                .reset_index(col_level=-1)
insp_tidy.columns = insp_tidy.columns.droplevel(0).rename(None)
insp_tidy.head()


# In[ ]:




