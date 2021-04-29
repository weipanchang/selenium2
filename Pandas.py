import numpy as np
from pandas_datareader import data as wb

ADBE = wb.DataReader('ADBE', data_source='yahoo', start='2020-1-1', end=('2021-4-28'))
print ADBE.head()
print ADBE.tail()