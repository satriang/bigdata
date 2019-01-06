#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[159]:


employee = pd.read_csv('data/employee.csv', index_col='RACE')
employee.head()


# In[ ]:




