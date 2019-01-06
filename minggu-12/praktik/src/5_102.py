#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[137]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
c1 = movie['content_rating'] == 'G'
c2 = movie['imdb_score'] < 4
criteria = c1 & c2
movie_loc = movie.loc[criteria]
movie_iloc = movie.iloc[criteria.values]
criteria_col = movie.dtypes == np.int64
cols = ['content_rating', 'imdb_score', 'title_year', 'gross']
col_index = [movie.columns.get_loc(col) for col in cols]
a = criteria.values
a[:5]


# In[ ]:




