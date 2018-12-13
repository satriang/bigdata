#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[14]:


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'title_year', 'imdb_score']]
movie3 = movie2.sort_values(['title_year','imdb_score'], ascending=False)
movie4 = movie[['movie_title', 'title_year', 'content_rating', 'budget']]
movie4_sorted = movie4.sort_values(['title_year', 'content_rating', 'budget'], 
                                   ascending=[False, False, True])
movie4_sorted.drop_duplicates(subset=['title_year', 'content_rating']).head(10)


# In[ ]:




