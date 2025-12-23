# Arithmetic
a = 10
b = 3

print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333335
print(a % b) # 1
print(a ** b) # 10 * 10 * 10 = 1000
print(a // b) # 3

print() # New line

# Comparison
x = 5
y = 10

print(x == y) # False
print(x != y) # True
print(x < y) # True
print(x > y) # False
print(x <= y) # True
print(x >= y) # False

print() # New line

# Logical
g = True
v = False

print(g and v) # False
print(g or v) # True
print(not g) # False

print() # New line

# Example 1
amount = 1200
tax = amount * 0.18
total = amount + tax
print(total) # 1416.0

if total > 1000:
    discount = total * 0.10
    total -= discount
print(total) # 1274.4

print() # New line

# Example 2
age = 65
student = 'yes'

if age >= 65 or student == 'yes': # Yes discount
    print("Yes discount")
else:
    print("No discount")