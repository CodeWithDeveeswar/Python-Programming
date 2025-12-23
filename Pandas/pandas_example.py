import pandas as pd

df = pd.read_csv("Pandas/data.csv")
df["Age"].to_csv("Pandas/output.csv", index=False)
print(df["Age"])
# 0    25
# 1    30
# 2    35
# Name: Age, dtype: int64
