#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[3]:


college = pd.read_csv('data/college.csv')
college.describe(include=[np.int64, np.float64]).T


# In[ ]:




