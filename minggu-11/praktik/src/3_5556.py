#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas_datareader as pdr


# In[5]:


def set_trailing_loss(symbol, purchase_date, perc):
    close = pdr.DataReader(symbol, 'yahoo', start=purchase_date)['Close']
    return close.cummax() * perc
msft_trailing_stop = set_trailing_loss('msft', '2017-6-1', .85)
msft_trailing_stop.head()


# In[ ]:




