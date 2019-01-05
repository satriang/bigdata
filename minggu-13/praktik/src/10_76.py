#!/usr/bin/env python
# coding: utf-8

# In[78]:


import pandas as pd
import numpy as np
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[110]:


crime = pd.read_hdf('data/crime.h5', 'crime').set_index('REPORTED_DATE')
import datetime
crime.between_time(datetime.time(2,0), datetime.time(5,0), include_end=False)


# In[ ]:




