import pandas as pd

df = pd.read_csv('data.csv')

grouped = df.groupby('City')['Age'].mean()

print(grouped)
