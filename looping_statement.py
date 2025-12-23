# For loop
names = ["saravana","gowtham","nandini","nila","rahul"]

for test in names:
    print(test.upper()) # SARAVANA
                        # GOWTHAM
                        # NANDINI
                        # NILA
                        # RAHUL

print() # New line

# While loop
correct_pin = '1234'
entered_pin = ''

while entered_pin != correct_pin:
    entered_pin = input("enter your correct pin: ")

print("access granted") # enter your correct pin: 1234
                        # access granted

print() # New line

# Break
nums = [1,2,3,4,9,6,7,8,5,10]

for i in nums:
    if i == 5:
        break
    print(i) # 1
             # 2
             # 3
             # 4
             # 9
             # 6
             # 7
             # 8

print() # New line

# Continue
n = [10,-5,7,-9,11]

for num in n:
    if num < 0:
        continue
    print(num) # 10
               # 7
               # 11

print() # New line

# Pass
n = [10,-5,7,-9,11]

for num in n:
    pass # Placeholder -> Future logic Implementation

print() # New line

# Use Case 1
count = 5

while count > 0:
    print(f"Countdown: {count}") # Countdown: 5
    count -= 1                   # Countdown: 4
                                 # Countdown: 3
print("Time's up!")              # Countdown: 2
                                 # Countdown: 1
                                 # Time's up!

print() # New line

# Use Case 2
items = []

while True:
    item = input("Add item (type 'done' to finish): ")
    if item.lower() == "done":
        break
    items.append(item)

print("Items in cart:", items) # Add item (type 'done' to finish): apple
                               # Add item (type 'done' to finish): banana
                               # Add item (type 'done' to finish): done
                               # Items in cart: ['apple', 'banana']
