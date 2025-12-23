deliver_name = "uzumaki NARUTO"

print(deliver_name.lower()) # uzumaki naruto
print(deliver_name.upper()) # UZUMAKI NARUTO
print(deliver_name.capitalize()) # Uzumaki naruto

print() # New line

# Use case 1
mobile = "9999999990"
masked = mobile[:2] + "******" + mobile[-2:]
print(masked) # 99******90

print() # New line

# Use case 2
song = "shape OF you"
artist = "ED sheeran"
formatted = f"{song.title()} - {artist.title()}"
print(formatted) # Shape Of You - Ed Sheeran

print() # New line

# Use case 3
location = "Chennai central"
fixed_location = location.replace("Chennai central", "Thambaram")
print(fixed_location) # Thambaram

print() # New line

# Use case 4
message = "your uber booking id is: UB12345. please keep it safe"
booking_id = message.split(":")[1].split(".")[0].strip() # Delimeter
print(booking_id) # UB12345

print() # New line

# Use case 5
promo_msg = "use ZOMOTO100 to get 100 offer on your first order"
if "ZOMOTO100" in promo_msg:
    print("offer applied") # offer applied

print() # New line

# Use case 6
feedback = "the driver was polite and the ride was smooth"
print("position is:", feedback.find("polite")) # position is: 15

print() # New line

# Use case 7
name = "deveeswar kandhan"
initials = "".join([word[0].upper() for word in name.split()])
print(initials) # DK

print() # New line

# Use case 8
dierty_input = "   airport   "
Clean = dierty_input.strip()
print(Clean) # airport

print() # New line

# Use case 9
word1 = "the trip was amazing and the car was clean"
word_count = len(word1.split())
print(word_count) # 9



