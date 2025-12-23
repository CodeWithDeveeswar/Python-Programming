# A Composed function is when the output of one function becomes the input of another - like f(g(x))

def add(x):
    return x + 2 # 4 + 2 = 6

def multi(x):
    return x * 2 # 2 * 2 = 4

def composed(x):
    return add(multi(x)) # f(g(x)) -> add of (x + 2)

print(composed(2)) # 6