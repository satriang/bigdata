#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[59]:


college = pd.read_csv('data/college.csv')
college[college['STABBR'] == 'TX'].head()


# In[ ]:




