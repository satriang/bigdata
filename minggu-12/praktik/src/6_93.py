#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[229]:


pd.options.display.max_rows= 40
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds = college.filter(like='UGDS_')
highest_percentage_race = college_ugds.idxmax(axis='columns')
highest_percentage_race.value_counts(normalize=True)


# In[ ]:




