#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[123]:


movie = pd.read_csv('data/movie.csv', index_col='movie_title')
c1 = movie['title_year'] >= 2010
c2 = movie['title_year'].isnull()
criteria = c1 | c2
movie_mask = movie.mask(criteria).dropna(how='all')
movie_boolean = movie[movie['title_year'] < 2010]
from pandas.testing import assert_frame_equal
assert_frame_equal(movie_boolean, movie_mask, check_dtype=False)


# In[124]:


get_ipython().run_line_magic('timeit', "movie.mask(criteria).dropna(how='all')")


# In[ ]:




