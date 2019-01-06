#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[193]:


employee = pd.read_csv('data/employee.csv')
dept_sal = employee[['DEPARTMENT', 'BASE_SALARY']]
dept_sal = dept_sal.sort_values(['DEPARTMENT', 'BASE_SALARY'],
                                ascending=[True, False])
max_dept_sal = dept_sal.drop_duplicates(subset='DEPARTMENT')


# In[199]:


employee['MAX_SALARY2'] = max_dept_sal['BASE_SALARY'].head(3)
employee.MAX_SALARY2.value_counts()


# In[ ]:




