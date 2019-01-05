#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


names = pd.read_csv('data/names.csv')
new_data_list = ['Aria', 1]
names.loc[4] = new_data_list
names.loc['five'] = ['Zach', 3]
names.loc[len(names)] = {'Name':'Zayd', 'Age':2}
names.loc[len(names)] = pd.Series({'Age':32, 'Name':'Dean'})
names


# In[ ]:




