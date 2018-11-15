import numpy as np

import pandas as pd

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data2))
print(pd.DataFrame(data2, index=['first', 'second']))
print(pd.DataFrame(data2, columns=['a', 'b']))