# Arithmetic Operators
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

# Comparison Operators
x = 5
y = 10

print(x == y) # False
print(x != y) # True
print(x < y) # True
print(x > y) # False
print(x <= y) # True
print(x >= y) # False

print() # New line

# Logical Operators
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

print() # New line

# Membership Operators
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)     # True
print('orange' in fruits)     # False
print('apple' not in fruits)  # False
print('grape' not in fruits)  # True

print() # New line

# Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2)      # True
print(list1 is list3)      # False
print(list1 is not list3)  # True

print() # New line

# Bitwise Operators
m = 5  # 0101 in binary
n = 3  # 0011 in binary
print(m & n)  # 1  (0001 in binary)
print(m | n)  # 7  (0111 in binary)
print(m ^ n)  # 6  (0110 in binary)
print(~m)     # -6 (inverts bits)
print(m << 1) # 10 (1010 in binary)
print(m >> 1) # 2  (0010 in binary)

print() # New line

# Assignment Operators
p = 10

p += 5    # p = p + 5
print(p)  # 15

p *= 2    # p = p * 2
print(p)  # 30

p -= 10   # p = p - 10
print(p)  # 20

p /= 4    # p = p / 4
print(p)  # 5.0

p %= 3    # p = p % 3
print(p)  # 2.0

p **= 3   # p = p ** 3
print(p)  # 8.0

p //= 2   # p = p // 2
print(p)  # 4.0

print() # New line

# Slice Operators
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:5])   # [2, 3, 4]
print(my_list[:4])    # [0, 1, 2, 3]
print(my_list[5:])    # [5, 6, 7, 8, 9]
print(my_list[-3:])   # [7, 8, 9]
print(my_list[::2])   # [0, 2, 4, 6, 8]
print(my_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(my_list[1:7:3]) # [1, 4]
