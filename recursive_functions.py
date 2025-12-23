# A Recursive function is a function that calls itself,
# in order to solve a smaller version of the same problem.

# Factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120

print() # New line

# Countdown
def countdown(n):
    if n == 0:
        print("🧨 Boom💥!")
        return
    print(n)
    countdown(n - 1)

print(countdown(5)) # 5
                    # 4
                    # 3
                    # 2
                    # 1
                    # 🧨 Boom💥!
                    # None