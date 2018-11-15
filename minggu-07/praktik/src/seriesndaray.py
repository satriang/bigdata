import numpy as np

import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

print (s[0])
print (s[:3])
print (s[s > s.median()])
print (s[[4, 3, 1]])
print (np.exp(s))
print (s['a'])

s['e'] = 12
print (s)

print ('e' in s)
print ('f' in s)

s.get('f')
print (s.get('f', np.nan))

print (s + s)
print (s*2)
print (np.exp(s))
print (s[1:] + s[:-1])