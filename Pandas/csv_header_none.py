import pandas as pd

# Specify header=None and pass column names
df = pd.read_csv("Pandas/dummy_data.csv", header=None, names=['Name', 'Age', 'Salary'])

print(df)