#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[49]:


names = pd.read_csv('data/names.csv')
names.index = ['Canada', 'Canada', 'USA', 'USA']
s = pd.Series({'Name': 'Zach', 'Age': 3}, name=len(names))
s


# In[ ]:




