#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[6]:


college = pd.read_csv('data/college.csv')
college['MENONLY'] = college['MENONLY'].astype('float16')
college['RELAFFIL'] = college['RELAFFIL'].astype('int8')
college.index = pd.Int64Index(college.index)
college.index.memory_usage()


# In[ ]:




