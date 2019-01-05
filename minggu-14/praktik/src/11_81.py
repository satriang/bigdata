#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[292]:


employee = pd.read_csv('data/employee.csv', 
                       parse_dates=['HIRE_DATE', 'JOB_DATE'])
import seaborn as sns
employee.groupby(['RACE', 'GENDER'], sort=False)['BASE_SALARY']         .mean().unstack('GENDER')         .plot(kind='bar', figsize=(16,4), rot=0,
              width=.8, cmap='Greys')


# In[ ]:




