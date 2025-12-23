uber_cities = ["Chennai", "Bangalore", "Chennai", "Delhi", "Bangalore"]

# Convert List To Set
unique_cities = set(uber_cities)
print(unique_cities) # {'Chennai', 'Delhi', 'Bangalore'}

print() # New line

uber_cities1 = {"Chennai", "Mumbai", "Bangalore"}
uber_cities2 = {"Bangalore", "Delhi", "Hyderabad"}

# Union
print(uber_cities1.union(uber_cities2)) # {'Chennai', 'Mumbai', 'Delhi', 'Hyderabad', 'Bangalore'}

print() # New line

# Intersection
print(uber_cities1.intersection(uber_cities2)) # {'Bangalore'}

print() # New line

# Difference
print(uber_cities1.difference(uber_cities2)) # {'Chennai', 'Mumbai'}
print(uber_cities2.difference(uber_cities1)) # {'Delhi', 'Hyderabad'}

print() # New line

# Add
uber_cities1.add("Pondicherry")
print(uber_cities1) # {'Chennai', 'Mumbai', 'Bangalore', 'Pondicherry'}

print() # New line

# Remove
uber_cities1.remove("Chennai")
print(uber_cities1) # {'Mumbai', 'Bangalore', 'Pondicherry'}

print() # New line

my_set = {1, 2, 3, 2}

print(my_set) # {1, 2, 3}

# Removes an element from a set without error if it is not present
my_set.discard(8)
print(my_set) # {1, 2, 3}

my_set.discard(3)
print(my_set) # {1, 2}



