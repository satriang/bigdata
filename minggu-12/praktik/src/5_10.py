#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[47]:


pd.options.display.max_columns = 50
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
movie_2_hours = movie['duration'] > 120
actors = movie[['actor_1_facebook_likes', 'actor_2_facebook_likes']].dropna()
(actors['actor_1_facebook_likes'] > actors['actor_2_facebook_likes']).mean()


# In[ ]:




