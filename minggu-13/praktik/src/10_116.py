#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[151]:


crime = pd.read_hdf('data/crime.h5', 'crime')
crime_table.loc[2017] = crime_table.loc[2017].div(.748).astype('int')
crime_table = crime_table.reindex(columns=days)
import seaborn as sns
sns.heatmap(crime_table, cmap='Greys')


# In[ ]:




