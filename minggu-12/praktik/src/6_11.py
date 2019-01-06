#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[148]:


college = pd.read_csv('data/college.csv')
columns = college.columns
c1 = columns[:4]
c1


# In[ ]:




