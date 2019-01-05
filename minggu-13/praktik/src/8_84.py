#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[65]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
sensors = pd.read_csv('data/sensors.csv')
sensors


# In[ ]:




