#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


bball_16 = pd.read_csv('data/baseball16.csv')
data_dict = bball_16.iloc[0].to_dict()
print(data_dict)


# In[ ]:




