#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[60]:


bball_16 = pd.read_csv('data/baseball16.csv')
data_dict = bball_16.iloc[0].to_dict()
new_data_dict = {k: '' if isinstance(v, str) else np.nan for k, v in data_dict.items()}


# In[61]:


random_data = []
for i in range(1000):
    d = dict()
    for k, v in data_dict.items():
        if isinstance(v, str):
            d[k] = np.random.choice(list('abcde'))
        else:
            d[k] = np.random.randint(10)
    random_data.append(pd.Series(d, name=i + len(bball_16)))
    
random_data[0].head()


# In[ ]:




