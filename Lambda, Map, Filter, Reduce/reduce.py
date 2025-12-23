from functools import reduce

nums = [10, 5, 22, 7]
maxi = reduce(lambda a, b : a if a > b else b, nums)
print(maxi) # 22