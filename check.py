import pandas as pd

df = pd.read_csv(
"Student_Performance.csv"
)

print(df.head())

print(df.isnull().sum())