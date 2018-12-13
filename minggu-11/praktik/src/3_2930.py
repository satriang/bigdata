#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[4]:


college = pd.read_csv('data/college.csv')
college['RELAFFIL'] = college['RELAFFIL'].astype(np.int8)
college.describe(include=['int', 'float']).T  # defaults to 64 bit int/floats


# In[ ]:




