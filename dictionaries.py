trip = {
    "trip_id" : "UB12345",
    "pickup" : "Chennai Central",
    "drop" : "Airport",
    "fare" : 430.70,
    "driver" : "Ravi",
    "status" : "Completed"
}

# Accessing By Key
print(trip["pickup"]) # Chennai Central

print() # New line

# Accessing By Get Method
print(trip.get("pickup"))  # Chennai Central
print(trip.get("Airport")) # None

print() # New line

# Print All Keys
print(trip.keys()) # dict_keys(['trip_id', 'pickup', 'drop', 'fare', 'driver', 'status'])

print() # New line

# Print All Values
print(trip.values()) # dict_values(['UB12345', 'Chennai Central', 'Airport', 430.7, 'Ravi', 'Completed'])

print() # New line

# Iterate
for key, value in trip.items():
    print(key, ":", value) # trip_id : UB12345
                           # pickup : Chennai Central
                           # drop : Airport
                           # fare : 430.7
                           # driver : Ravi
                           # status : Completed

print() # New line

# Update
trip.update({"car_model" : "Suzuki"})
print(trip) # {'trip_id': 'UB12345', 'pickup': 'Chennai Central', 'drop': 'Airport', 'fare': 430.7, 'driver': 'Ravi', 'status': 'Completed', 'car_model': 'Suzuki'}

trip.update({"car_model" : "Ford"})
print(trip) # {'trip_id': 'UB12345', 'pickup': 'Chennai Central', 'drop': 'Airport', 'fare': 430.7, 'driver': 'Ravi', 'status': 'Completed', 'car_model': 'Ford'}

print() # New line

# Pop
trip.pop("status")
print(trip) # {'trip_id': 'UB12345', 'pickup': 'Chennai Central', 'drop': 'Airport', 'fare': 430.7, 'driver': 'Ravi', 'car_model': 'Ford'}

print() # New line

# Duplicate Check
trip = {
    "trip_id" : "UB12345",
    "pickup" : "Chennai Central",
    "drop" : "Airport",
    "fare" : 430.70,
    "driver" : "Ravi",
    "status" : "Completed",
    "trip_id" : "UB67890"
}

for k, v in trip.items():
    print(k, ":", v) # trip_id : UB67890
                     # pickup : Chennai Central
                     # drop : Airport
                     # fare : 430.7
                     # driver : Ravi
                     # status : Completed

print() # New line

# Multiple Values
trip = {
    "trip_id" : "UB12345",
    "pickup" : "Chennai Central",
    "drop" : ["Airport", "Tambaram", "Medavakkam"],
    "fare" : 430.70,
    "driver" : "Ravi",
    "status" : "Completed",
}

for k, v in trip.items():
    print(k, ":", v) # trip_id : UB12345
                     # pickup : Chennai Central
                     # drop : ['Airport', 'Tambaram', 'Medavakkam']
                     # fare : 430.7
                     # driver : Ravi
                     # status : Completed

print() # New line

# Accessing The Single Value From Multiple Values of Key Using Index Number
print(trip["drop"][1]) # Tambaram

print() # New line

# Iterate The Multiple Values of Key
for location in trip["drop"]:
    print(location) # Airport
                    # Tambaram
                    # Medavakkam

print() # New line

# Multiple Records Using Nested Dictionaries
trips = {
    "UB001": {"trip_id" : "UB001", "pickup" : "Chennai", "drop" : "Airport", "fare" : 430},
    "UB002": {"trip_id" : "UB002", "pickup" : "Tambaram", "drop" : "Central", "fare" : 320},
    "UB003": {"trip_id" : "UB003", "pickup" : "T-Nagar", "drop" : "Velachery", "fare" : 210}
}

# Lookup the fare for trip "UB001" using nested dictionary access
print("UB001 Fare:", trips["UB001"]["fare"]) # UB001 Fare: 430

print() # New line

# Loop through all trips in the dictionary
for trip_id, details in trips.items():
    print(trip_id)
    print(details["pickup"], "->", details["drop"]) # UB001
                                                    # Chennai -> Airport
                                                    # UB002
                                                    # Tambaram -> Central
                                                    # UB003
                                                    # T-Nagar -> Velachery