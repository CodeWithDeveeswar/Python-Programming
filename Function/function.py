# Function with no argument
def great():
    print("Welcome to function")

great()

print() # New line

# Function with one argument
def great(name):
    print(f"Hello {name}, welcome!")

great("Deveeswar") # Hello Deveeswar, welcome!

print() # New line

# Function with two argument
def add(a, b):
    print(a + b)

add(4,5) # 9

print() # New line

# Using return
def add(a, b):
    return (a + b)

result = add(1,4)
print(result) # 5

print() # New line

# Import function
from add_function import add

result = add(10, 20)

print(result / 10) # 3.0

print() # New line

# Using *args for any (multiple) number of argument
def add(*args):
    total = 0
    for num in args:
        total += num

    return total

print(add(1, 2))    # 3
print(add(1, 2, 3)) # 6

print() # New line

# Using **kwargs for key, value pair and also multiple number of argument
def create_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

create_profile(Name="Deveeswar", Age=23, Job="Data engineer")
# User Profile
# Name : Deveeswar
# Age : 23
# Job : Data engineer




