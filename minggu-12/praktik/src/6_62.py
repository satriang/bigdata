#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[201]:


pd.options.display.max_rows = 8
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college.dtypes


# In[ ]:




