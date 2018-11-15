import numpy as np

import pandas as pd

d = {'one' : [1., 2., 3., 4.],
         'two' : [4., 3., 2., 1.]}

print (pd.DataFrame(d))
print (pd.DataFrame(d, index=['a', 'b', 'c', 'd']))