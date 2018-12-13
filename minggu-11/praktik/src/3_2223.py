#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[23]:


college = pd.read_csv('data/college.csv')
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)

