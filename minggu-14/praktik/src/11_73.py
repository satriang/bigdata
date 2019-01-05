#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[285]:


meetup = pd.read_csv('data/meetup_groups.csv', 
                     parse_dates=['join_date'], 
                     index_col='join_date')
group_count = meetup.groupby([pd.Grouper(freq='W'), 'group']).size()
gc2 = group_count.unstack('group', fill_value=0)
group_total = gc2.cumsum()
row_total = group_total.sum(axis='columns')
group_cum_pct = group_total.div(row_total, axis='index')
pie_data = group_cum_pct.asfreq('3MS', method='bfill')                         .tail(6).to_period('M').T
from matplotlib.cm import Greys
greys = Greys(np.arange(50,250,40))

ax_array = pie_data.plot(kind='pie', subplots=True, 
                         layout=(2,3), labels=None,
                         autopct='%1.0f%%', pctdistance=1.22,
                         colors=greys)
ax1 = ax_array[0, 0]
ax1.figure.legend(ax1.patches, pie_data.index, ncol=3)
for ax in ax_array.flatten():
    ax.xaxis.label.set_visible(True)
    ax.set_xlabel(ax.get_ylabel())
    ax.set_ylabel('')
ax1.figure.subplots_adjust(hspace=.3)


# In[ ]:




