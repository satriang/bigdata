#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[41]:


pd.options.display.max_columns = 50
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
movie_2_hours = movie['duration'] > 120
movie_2_hours.head(10)


# In[ ]:




