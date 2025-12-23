def calculate_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)

print(calculate_price(1000, 0.18)) # 1180.0
print(calculate_price(500, 0.18))  # 590.0
