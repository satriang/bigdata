#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[18]:


state_fruit2 = pd.read_csv('data/state_fruit2.csv')
state_fruit2.melt(id_vars='State')


# In[ ]:




