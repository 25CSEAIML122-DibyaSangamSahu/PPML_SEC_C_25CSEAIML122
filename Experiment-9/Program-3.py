#Question : WAP to read CSV and JSON files.

#Answer :
import pandas as pd
print(pd.read_csv('sample.csv'))
print(pd.read_json('sample.json'))