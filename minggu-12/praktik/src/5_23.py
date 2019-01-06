#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[61]:


college = pd.read_csv('data/college.csv')
college2 = college.set_index('STABBR')
get_ipython().run_line_magic('timeit', "college[college['STABBR'] == 'TX']")


# In[ ]:




