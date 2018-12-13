#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
state_fruit.stack()           .rename_axis(['state', 'fruit'])           .reset_index(name='weight')


# In[ ]:




