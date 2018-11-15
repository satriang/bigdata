import numpy as np

import pandas as pd

s = pd.Series(np.random.randn(5), name='something')

print (s)
print (s.name)

s2 = s.rename("different")
print (s2.name)