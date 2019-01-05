#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[54]:


bball_16 = pd.read_csv('data/baseball16.csv')
data_dict = bball_16.iloc[0].to_dict()
new_data_dict = {k: '' if isinstance(v, str) else np.nan for k, v in data_dict.items()}
print(new_data_dict)


# In[ ]:




