#Question : WAP to create and work with a Pandas series.

#Answer :
import pandas as pd
S = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(S)
print(S['a'])

#Output:
'''a    10
b    20
c    30
dtype: int64
10'''