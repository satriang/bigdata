import numpy as np

import pandas as pd

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'), (2,3.,"World")]

print (pd.DataFrame(data))

print (pd.DataFrame(data, index=['first', 'second']))

print (pd.DataFrame(data, columns=['C', 'A', 'B']))