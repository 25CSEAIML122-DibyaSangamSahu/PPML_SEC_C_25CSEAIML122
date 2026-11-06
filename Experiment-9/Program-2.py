#Question : WAP to create and manipulate a data frame.

import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
print(df)
print(df['Age'])
print(df.iloc[1])

#Output:
'''Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35
0    25
1    30
2    35
Name: Age, dtype: int64
Name    Bob
Age      30
Name: 1, dtype: object'''