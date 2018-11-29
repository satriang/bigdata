#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[12]:


college_dd = pd.read_csv('data/college_data_dictionary.csv')


# In[13]:


with pd.option_context('display.max_rows', 8):
    display(college_dd)


# In[ ]:




