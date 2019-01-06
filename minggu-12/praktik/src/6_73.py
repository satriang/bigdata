#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[212]:


pd.options.display.max_rows = 8
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_n = college.select_dtypes(include=[np.number])
criteria = college_n.nunique() == 2
binary_cols = college_n.columns[criteria].tolist()
college_n2 = college_n.drop(labels=binary_cols, axis='columns')
max_cols = college_n2.idxmax()
unique_max_cols = max_cols.unique()
college_n2.loc[unique_max_cols].style.highlight_max()


# In[ ]:




