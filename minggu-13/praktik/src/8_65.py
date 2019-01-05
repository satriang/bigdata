#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[44]:


usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
weightlifting = pd.read_csv('data/weightlifting_men.csv')
wl_melt = weightlifting.melt(id_vars='Weight Category', 
                             var_name='sex_age', 
                             value_name='Qual Total')
sex_age['Sex'] = sex_age['Sex'].str[0]
wl_cat_total = wl_melt[['Weight Category', 'Qual Total']]
wl_tidy = pd.concat([sex_age, wl_cat_total], axis='columns')
cols = ['Weight Category', 'Qual Total']
sex_age[cols] = wl_melt[cols]
age_group = wl_melt.sex_age.str.extract('(\d{2}[-+](?:\d{2})?)', expand=False)
sex = wl_melt.sex_age.str[0]
new_cols = {'Sex':sex, 
            'Age Group': age_group}
wl_tidy2 = wl_melt.assign(**new_cols).drop('sex_age', axis='columns')
wl_tidy2.head()


# In[ ]:




