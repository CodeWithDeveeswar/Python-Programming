# A Generator function is a special type of function that uses yield keyword,
# to return values one by one, instead of returning everything at once.

def get_numbers(n):
    for i in range(n):
        yield i # Pauses here

for num in get_numbers(10):
    print(num) # 0
               # 1
               # 2
               # 3
               # 4
               # 5
               # 6
               # 7
               # 8
               # 9
