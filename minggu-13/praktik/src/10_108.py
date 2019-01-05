#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[141]:


crime = pd.read_hdf('data/crime.h5', 'crime')
wd_counts = crime['REPORTED_DATE'].dt.weekday_name.value_counts()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
title = 'Denver Crimes and Traffic Accidents per Year' 
crime['REPORTED_DATE'].dt.year.value_counts()                               .sort_index()                               .plot(kind='barh', title=title)


# In[ ]:




