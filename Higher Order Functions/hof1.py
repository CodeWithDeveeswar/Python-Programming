# HOF Type 1: Takes another function as an argument

def gmail_email(username, domain="gmail.com"):
    return f"{username}@{domain}"

def ymail_email(username, domain="ymail.com"):
    return f"{username}@{domain}"

def hotmail_email(username, domain="hotmail.com"):
    return f"{username}@{domain}"


def build_email(username, email_func):
    return email_func(username) # gmail_email("deveeswar")

print(build_email("deveeswar", gmail_email))    # deveeswar@gmail.com
print(build_email("barath", ymail_email))       # barath@ymail.com
print(build_email("velmurugan", hotmail_email)) # velmurugan@hotmail.com

