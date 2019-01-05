#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[192]:


crime_sort = pd.read_hdf('data/crime.h5', 'crime')                .set_index('REPORTED_DATE')                .sort_index()
crime_sort = crime_sort[:'2017-8']
ad_period = crime_sort.groupby([lambda x: x.to_period('M'), 
                                'OFFENSE_CATEGORY_ID']).size()
ad_period = ad_period.sort_values()                      .reset_index(name='Total')                      .rename(columns={'level_0':'REPORTED_DATE'})
aug_2018 = pd.Period('2017-8', freq='M')
goal_period = ad_period[ad_period['REPORTED_DATE'] == aug_2018].reset_index(drop=True)
goal_period['Total_Goal'] = goal_period['Total'].mul(.8).astype(int)

pd.merge_asof(goal_period, ad_period, left_on='Total_Goal', right_on='Total', 
                  by='OFFENSE_CATEGORY_ID', suffixes=('_Current', '_Last')).head()


# In[ ]:




