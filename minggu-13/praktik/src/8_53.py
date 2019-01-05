#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[29]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college = pd.read_csv('data/college.csv')
cg = college.groupby(['STABBR', 'RELAFFIL'])['UGDS', 'SATMTMID']             .agg(['count', 'min', 'max']).head(6)
cg = cg.rename_axis(['AGG_COLS', 'AGG_FUNCS'], axis='columns')
cg.stack('AGG_FUNCS')   .swaplevel('AGG_FUNCS', 'STABBR', axis='index')   .sort_index(level='RELAFFIL', axis='index')   .sort_index(level='AGG_COLS', axis='columns').head(6)


# In[ ]:




