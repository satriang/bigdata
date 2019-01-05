#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[10]:


state_fruit2 = pd.read_csv('data/state_fruit2.csv')
state_fruit2.set_index('State').stack()


# In[ ]:




