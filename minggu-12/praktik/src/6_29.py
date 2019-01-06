#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[166]:


employee = pd.read_csv('data/employee.csv', index_col='RACE')
salary1 = employee['BASE_SALARY']
salary2 = employee['BASE_SALARY']
salary1 = salary1.sort_index()
salary_add = salary1 + salary2
salary_add1 = salary1 + salary1
len(salary1), len(salary2), len(salary_add), len(salary_add1)


# In[ ]:




