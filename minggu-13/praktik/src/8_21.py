#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[22]:


movie = pd.read_csv('data/movie.csv')
stubs = ['actor', 'actor_facebook_likes']
actor2_tidy = pd.wide_to_long(actor2, 
                              stubnames=stubs, 
                              i=['movie_title'], 
                              j='actor_num', 
                              sep='_').reset_index()
actor2_tidy.head()


# In[ ]:




