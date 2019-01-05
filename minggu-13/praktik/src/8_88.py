#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[6]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
movie = pd.read_csv('data/movie_altered.csv')
movie.head()


# In[ ]:




