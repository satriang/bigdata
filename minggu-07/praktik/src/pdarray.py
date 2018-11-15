import numpy as np

import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
d = {'b' : 1, 'a' : 0, 'c' : 2}
e = {'a' : 0., 'b' : 1., 'c' : 2.}


print (s)
print (s.index)
print (pd.Series(np.random.randn(5)))
print (pd.Series(d))
print (pd.Series(d, index=['b', 'c', 'd', 'a']))
print (pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))