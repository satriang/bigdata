#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


# In[2]:


college = pd.read_csv('data/college.csv')


# In[8]:


with pd.option_context('display.max_rows', 5):
    display(college.describe(include=[np.number], 
                 percentiles=[.01, .05, .10, .25, .5, .75, .9, .95, .99]).T)


# In[ ]:




