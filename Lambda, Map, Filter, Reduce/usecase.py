from functools import reduce

price = [250, 900, 1200, 400, 1500]
expensive = list(filter(lambda x: x > 1000, price))
total = reduce(lambda a, b : a + b, expensive)
print(total) # 2700