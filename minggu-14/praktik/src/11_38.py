#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[234]:


movie = pd.read_csv('data/movie.csv')
top10 = movie.sort_values('budget', ascending=False)              .groupby('title_year')['budget']              .apply(lambda x: x.iloc[:10].median() / 1e6)
        
top10_roll = top10.rolling(5, min_periods=1).mean()
top10_roll.tail()


# In[ ]:




