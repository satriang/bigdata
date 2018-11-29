#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


# In[2]:


college = pd.read_csv('data/college.csv')


# In[3]:


with pd.option_context('display.max_rows', 8):
    display(college.describe(include=[np.number]).T)


# In[ ]:




