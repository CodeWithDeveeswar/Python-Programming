import sys

if len(sys.argv) == 2:
    print("Usage: python email_generator.py 'Full Name and Last Name'")
    sys.exit()

full_name = " ".join(sys.argv[1:])

# Format the name
email = full_name.lower().replace(" ", ".") + "@company.com"

# Output
print("\n--- Your Profile ---")
print("Full Name:", full_name)   # Output: Full Name: Devesh K
print("Generated Email:", email) # Output: Generated Email: devesh.k@company.com

# Terminal command:  python .\Input\email_generator_using_sys.argv.py Devesh K
