import pandas as pd

df = pd.DataFrame({'x': [1, 2, 3, 4, 5]})

result = df[df['x'] > 3] # This runs immediately

print(result)
#    x
# 3  4
# 4  5