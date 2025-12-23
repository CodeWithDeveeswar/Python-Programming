total = 5

def add(amount):
    total = 0
    total += amount
    print("I am from add():", total)

def test():
    print("I am from test():", total)

add(10) # I am from add(): 10
test()  # I am from test(): 0