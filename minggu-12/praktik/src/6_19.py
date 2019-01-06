#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[156]:


s1 = pd.Series(index=list('aaab'), data=np.arange(4))
s2 = pd.Series(index=list('cababb'), data=np.arange(6))
s1 + s2


# In[ ]:




