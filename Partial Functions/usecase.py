from functools import partial

def create_email(username, domain):
    return f"{username}@{domain}"

gmail = partial(create_email, domain = "gmail.com")
hotmail = partial(create_email, domain = "hotmail.com")

print(gmail("deveeswar")) # deveeswar@gmail.com
print(hotmail("barath"))  # barath@hotmail.com



