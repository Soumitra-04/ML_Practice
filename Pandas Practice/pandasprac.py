import numpy as np
import pandas as pd

#creating a Series(1D array holding any data)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# print(s.dtype) #not needed, implicitly printed

#creating a DataFrame
 
#create a DatetimeIndex of size from 2013-01-01 with freq of 1 year
dates = pd.date_range("20130101", periods= 6,freq = 'Y')
print(dates)
#create a DataFrame 
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("WXYZ"))
print(df)