import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv('Pandas/sales.csv')

# Display the DataFrame
print(df)

# Save DataFrame to JSON
df.to_json("Pandas/sales.json", orient='records', indent=2)