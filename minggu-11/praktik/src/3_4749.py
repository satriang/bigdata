#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas_datareader as pdr


# In[2]:


tsla = pdr.DataReader('tsla', data_source='yahoo',start='2017-1-1')
tsla.head(8)


# In[ ]:




