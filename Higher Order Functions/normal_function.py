def build_email(username, provider):
    if provider == "gmail":
        return f"{username}@gmail.com"
    elif provider == "ymail":
        return f"{username}@ymail.com"
    elif provider == "hotmail":
        return f"{username}@hotmail.com"
    else:
        return f"{username}@example.com"

print(build_email("deveeswar", "gmail"))    # deveeswar@gmail.com
print(build_email("barath", "ymail"))       # barath@ymail.com
print(build_email("velmurugan", "hotmail")) # velmurugan@hotmail.com
print(build_email("kavinkumar", "unknown")) # kavinkumar@example.com