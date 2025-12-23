try:
    number_of_items = int(input("How many items? ")) # How many items? 5
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("Total price:", total_price)      # Total price: 1000
    print("Average price:", average_price)  # Average price: 200.0
except ZeroDivisionError:
    print("❌ You cannot order 0 items.")
finally:
    print("Always Execute") # Always Execute

print("✅ Next Code Block") # Always Execute