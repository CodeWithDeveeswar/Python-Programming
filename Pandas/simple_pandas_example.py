import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Landon', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    Landon
# 2  Charlie   35    Mumbai

print() # Newline

print(df['Name'])
# 0      Alice
# 1        Bob
# 2    Charlie
# Name: Name, dtype: object

print() # Newline

print(df.dtypes)
# Name    object
# Age      int64
# City    object
# dtype: object