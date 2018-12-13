#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas_datareader as pdr


# In[3]:


tsla = pdr.DataReader('tsla', data_source='yahoo',start='2017-1-1')
tsla_close = tsla['Close']
tsla_cummax = tsla_close.cummax()
tsla_cummax.head(8)


# In[ ]:




