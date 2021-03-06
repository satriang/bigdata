#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[284]:


meetup = pd.read_csv('data/meetup_groups.csv', 
                     parse_dates=['join_date'], 
                     index_col='join_date')
group_count = meetup.groupby([pd.Grouper(freq='W'), 'group']).size()
gc2 = group_count.unstack('group', fill_value=0)
group_total = gc2.cumsum()
row_total = group_total.sum(axis='columns')
group_cum_pct = group_total.div(row_total, axis='index')
pie_data = group_cum_pct.asfreq('3MS', method='bfill')                         .tail(6).to_period('M').T
pie_data


# In[ ]:




