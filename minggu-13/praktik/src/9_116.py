#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


from IPython.display import display_html
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data/chinook.db')
pd.read_sql_query('select * from tracks limit 5', engine)


# In[ ]:




