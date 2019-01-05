#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[32]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
movie = pd.read_csv('data/movie_altered.csv')
movie.insert(0, 'id', np.arange(len(movie)))
stubnames = ['director', 'director_fb_likes', 'actor', 'actor_fb_likes']
movie_long = pd.wide_to_long(movie, 
                                 stubnames=stubnames, 
                                 i='id', 
                                 j='num', 
                                 sep='_').reset_index()
movie_long['num'] = movie_long['num'].astype(int)
movie_table = movie_long[['id','title', 'year', 'duration', 'rating']]
director_table = movie_long[['id', 'director', 'num', 'director_fb_likes']]
actor_table = movie_long[['id', 'actor', 'num', 'actor_fb_likes']]
movie_table = movie_table.drop_duplicates().reset_index(drop=True)
director_table = director_table.dropna().reset_index(drop=True)
actor_table = actor_table.dropna().reset_index(drop=True)
movie_table.memory_usage(deep=True).sum() + director_table.memory_usage(deep=True).sum() + actor_table.memory_usage(deep=True).sum()
director_cat = pd.Categorical(director_table['director'])
director_table.insert(1, 'director_id', director_cat.codes)

actor_cat = pd.Categorical(actor_table['actor'])
actor_table.insert(1, 'actor_id', actor_cat.codes)
director_associative = director_table[['id', 'director_id', 'num']]
dcols = ['director_id', 'director', 'director_fb_likes']
director_unique = director_table[dcols].drop_duplicates().reset_index(drop=True)
actor_associative = actor_table[['id', 'actor_id', 'num']]
acols = ['actor_id', 'actor', 'actor_fb_likes']
actor_unique = actor_table[acols].drop_duplicates().reset_index(drop=True)


# In[36]:


actors = actor_associative.merge(actor_unique, on='actor_id')                           .drop('actor_id', 1)                           .pivot_table(index='id', columns='num', aggfunc='first')

actors.columns = actors.columns.get_level_values(0) + '_' +                  actors.columns.get_level_values(1).astype(str)

directors = director_associative.merge(director_unique, on='director_id')                           .drop('director_id', 1)                           .pivot_table(index='id', columns='num', aggfunc='first')

directors.columns = directors.columns.get_level_values(0) + '_' +                     directors.columns.get_level_values(1).astype(str)
movie2 = movie_table.merge(directors.reset_index(), on='id', how='left')                     .merge(actors.reset_index(), on='id', how='left')
movie.equals(movie2[movie.columns])


# In[ ]:




