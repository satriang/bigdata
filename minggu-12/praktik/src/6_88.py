#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[225]:


college = pd.read_csv('data/college.csv', index_col='INSTNM')

cols = ['MD_EARN_WNE_P10', 'GRAD_DEBT_MDN_SUPP']
for col in cols:
    college[col] = pd.to_numeric(college[col], errors='coerce')

college_n = college.select_dtypes(include=[np.number])
criteria = college_n.nunique() == 2
binary_cols = college_n.columns[criteria].tolist()
college_n = college_n.drop(labels=binary_cols, axis='columns')
has_row_max = college_n.eq(college_n.max()).any(axis='columns')
pd.options.display.max_rows=6
has_row_max2 = college_n.eq(college_n.max())                        .cumsum()                        .cumsum()                        .eq(1)                        .any(axis='columns')
idxmax_cols = has_row_max2[has_row_max2].index
get_ipython().run_line_magic('timeit', 'college_n.idxmax().values')


# In[ ]:




