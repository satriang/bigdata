#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[116]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
fb_likes = movie['actor_1_facebook_likes'].dropna()
criteria_high = fb_likes < 20000
criteria_low = fb_likes > 300
fb_likes_cap = fb_likes.where(criteria_high, other=20000)                       .where(criteria_low, 300)
fb_likes_cap2 = fb_likes.clip(lower=300, upper=20000)
fb_likes_cap2.equals(fb_likes_cap)


# In[ ]:




