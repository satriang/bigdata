#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[80]:


stocks_2016 = pd.read_csv('data/stocks_2016.csv', index_col='Symbol')
stocks_2017 = pd.read_csv('data/stocks_2017.csv', index_col='Symbol')
s_list = [stocks_2016, stocks_2017]
pd.concat(s_list, keys=['2016', '2017'], axis='columns', names=['Year', None])


# In[ ]:




