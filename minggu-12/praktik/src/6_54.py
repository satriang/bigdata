#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[188]:


employee = pd.read_csv('data/employee.csv')
max_dept_sal = max_dept_sal.set_index('DEPARTMENT')
employee = employee.set_index('DEPARTMENT')
employee['MAX_DEPT_SALARY'] = max_dept_sal['BASE_SALARY']
pd.options.display.max_columns = 6
employee.head()


# In[ ]:




