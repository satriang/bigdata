#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


from IPython.display import display_html
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data/chinook.db')
tracks = pd.read_sql_table('tracks', engine)
genres = pd.read_sql_table('genres', engine)
genres.head()


# In[ ]:




