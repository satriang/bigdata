#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[184]:


df_14 = baseball_14[['G','AB', 'R', 'H']]
df_15 = baseball_15[['AB', 'R', 'H', 'HR']]
df_14.add(df_15, fill_value=0).head(10).style.highlight_null('yellow')


# In[ ]:




