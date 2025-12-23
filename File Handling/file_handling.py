file = open("File Handling/notes.txt", "w")
file.write("Welcome to Python File Handling!\n")
file.write("This is a new file.\n")
file.close()

file = open("File Handling/notes.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close() # File Content:
             #  Welcome to Python File Handling!
             # This is a new file.

file = open("File Handling/notes.txt", "a")
file.write("Adding a new line.\n")
file.close()

'''
file = open("File Handling/notes.txt", "w")
file.write("Adding a new line2.\n")
file.close()
'''

with open("File Handling/notes.txt", "r") as file:
    for line in file:
        print(line.strip()) # Welcome to Python File Handling!
                            # This is a new file.
                            # Adding a new line.

print() # New line

with open("File Handling/data.txt", "r") as file:
    print(file.readline().strip()) # Apple
    print(file.readline().strip()) # Orange
    print(file.readline().strip()) # Banana

print() # New line

with open("File Handling/file.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if "ERROR" in line:
            print("Found error:", line.strip())
            # Found error: ERROR: Failed to connect to database
            # Found error: ERROR: Null pointer exception occurred

print() # New line

with open("File Handling/file.txt") as f:
    for _ in range(5):
        print(f.readline().strip()) # INFO: Application started successfully
                                    # INFO: User login completed
                                    # WARNING: Disk space low
                                    # ERROR: Failed to connect to database
                                    # INFO: Scheduled task started

print() # New line

# Using csv file
with open("File Handling/input_file.csv", "r") as infile, open("File Handling/output_file.csv", "w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line) # id,name,age
                            # 1,John,25
                            # 2,Alice,30
                            # 4,Bob,22

print() # New line

# Print age column using dictionary
import csv

with open("File Handling/input_file.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["age"]) # 25
                          # 30
                          # 22

print() # New line

# Print name column using array of index
with open("File Handling/input_file.csv", "r") as file:
    lines = file.readlines()
    for line in lines[1:]: # Skip header
        columns = line.strip().split(",")
        # columns[0], columns[1], columns[2]
        # id, name, age
        print(columns[1]) #John
                          # Alice
                          # Bob


