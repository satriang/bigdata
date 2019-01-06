#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[50]:


pd.options.display.max_columns = 50
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
criteria1 = movie.imdb_score > 8
criteria2 = movie.content_rating == 'PG-13'
criteria3 = (movie.title_year < 2000) | (movie.title_year >= 2010)

criteria_final = criteria1 & criteria2 & criteria3
criteria_final.head()


# In[ ]:




