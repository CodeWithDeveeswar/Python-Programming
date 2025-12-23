# Creating lists for different apps
playlist = ["Shap of You", "Naa Ready", "Believer", "Tum Hi Ho"] # Spotify
favourite_food = ["Pizza", "Burger", "Dosa", "Biryani"] # Zomato
recent_location = ["Home", "Airport", "Work", "Mall"] # Uber

print("Spotify Playlist:", playlist)      # Spotify Playlist: ['Shap of You', 'Naa Ready', 'Believer', 'Tum Hi Ho']
print("Zomato Foods:", favourite_food)    # Zomato Foods: ['Pizza', 'Burger', 'Dosa', 'Biryani']
print("Uber Locations:", recent_location) # Uber Locations: ['Home', 'Airport', 'Work', 'Mall']

print() # New line

# List Methods
playlist.append("Oo Solriya")
print("After Append:", playlist) # After Append: ['Shap of You', 'Naa Ready', 'Believer', 'Tum Hi Ho', 'Oo Solriya']

playlist.insert(1, "Oorum Blood")
print("After Insert:", playlist) # After Insert: ['Shap of You', 'Oorum Blood', 'Naa Ready', 'Believer', 'Tum Hi Ho', 'Oo Solriya']

playlist.remove("Naa Ready")
print("After removing:", playlist) # After removing: ['Shap of You', 'Oorum Blood', 'Believer', 'Tum Hi Ho', 'Oo Solriya']

playlist.pop()
print("After Pop:", playlist) # After Pop: ['Shap of You', 'Oorum Blood', 'Believer', 'Tum Hi Ho']

playlist.reverse()
print("After Reverse:", playlist) # After Reverse: ['Tum Hi Ho', 'Believer', 'Oorum Blood', 'Shap of You']

print("Count of Believer:", playlist.count('Believer')) # Count of Believer: 1

print() # New line

# List Slicing
print("Top 2 Songs:", playlist[0:2]) # Top 2 Songs: ['Tum Hi Ho', 'Believer']

print("Top 2 Locations:", recent_location[-2:]) # Top 2 Locations: ['Work', 'Mall']

print() # New line

# List Iteration
for food in favourite_food:
    print("Food:", food) # Food: Pizza
                         # Food: Burger
                         # Food: Dosa
                         # Food: Biryani

print() # New line

artists = ["Arijit Singh", "Imagine Dragons", "Sai Abhyankkar", "Ed Sheeran"]
for i in range(len(playlist)):
    print(playlist[i] + " - " + artists[i]) # Tum Hi Ho - Arijit Singh
                                            # Believer - Imagine Dragons
                                            # Oorum Blood - Sai Abhyankkar
                                            # Shap of You - Ed Sheeran

print() # New line

# Check If
if "Dosa" in favourite_food:
    print("Yes") # Yes

print() # New line

# Update
favourite_food[1] = "Shawarma"
print(favourite_food) # ['Pizza', 'Shawarma', 'Dosa', 'Biryani']

print() # New line

# Mixed DataType
mixed = ["Devesh", 23, 8.17]

for m in mixed:
    print(m) # Devesh
             # 23
             # 8.17

print() # New line

# Enumerate 
for i, location in enumerate(recent_location):
    print(f"Location {i}: {location}") # Location 0: Home
                                       # Location 1: Airport
                                       # Location 2: Work
                                       # Location 3: Mall