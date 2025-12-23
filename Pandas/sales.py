import pandas as pd

# Step 1: Read the file
df = pd.read_csv("Pandas/sales.csv")

# Step 2: Add one new column for Total
df['Total'] = df['Price'] * df['Quantity']

# Step 3: Group by product
grouped = df.groupby('Product')['Total'].sum().reset_index()

# Step 4: Sort by total sales
sorted_df = grouped.sort_values(by='Total', ascending=False)

# Output
print("Sales Summary")
print(sorted_df)
# Sales Summary
#   Product  Total
# 0    Pant   3200
# 1   Shirt   1500
