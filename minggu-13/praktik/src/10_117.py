#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[152]:


denver_pop = pd.read_csv('data/denver_pop.csv', index_col='Year')
denver_pop


# In[ ]:




