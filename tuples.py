trip_summary = ("UberGo", "Chennai", "Airport", 450.00, "Completed")

print(trip_summary) # ('UberGo', 'Chennai', 'Airport', 450.0, 'Completed')

print() # New line

# Access By Index
print(trip_summary[1]) # Chennai

print() # New line

# Loop Through
for item in trip_summary:
    print(item) # UberGo
                # Chennai
                # Airport
                # 450.0
                # Completed

print() # New line

# Find Length
print("Length:", len(trip_summary)) # Length: 5

print() # New line

# Count And Index
print("Count of 'Complete':", trip_summary.count("Completed")) # Count of 'Complete': 1
print("Index of 'Airport':", trip_summary.index("Airport"))    # Index of 'Airport': 2

