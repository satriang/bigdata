#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[38]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
weightlifting = pd.read_csv('data/weightlifting_men.csv')
wl_melt = weightlifting.melt(id_vars='Weight Category', 
                             var_name='sex_age', 
                             value_name='Qual Total')
sex_age['Sex'] = sex_age['Sex'].str[0]
sex_age.head()

