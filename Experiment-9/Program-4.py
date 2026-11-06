#Question : WAP to calculate the correlation between columns in a data frame.

#Answer :
import pandas as pd
df = pd.DataFrame({
    'Math': [90, 85, 80, 95],
    'Science': [88, 82, 85, 90],
    'English': [78, 75, 80, 85]
})
print(df.corr())

#Output:
'''Math   Science   English
Math     1.000000  0.982708  0.912871
Science  0.982708  1.000000  0.923412
English  0.912871  0.923412  1.000000'''