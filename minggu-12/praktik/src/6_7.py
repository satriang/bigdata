#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[144]:


college = pd.read_csv('data/college.csv')
columns = college.columns
columns.min(), columns.max(), columns.isnull().sum()


# In[ ]:




