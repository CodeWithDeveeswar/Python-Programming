# HOF Type 2: Returns a function as its output

def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email

# Pre-bounded function (Context bound or Pre-bound logic)
gmail = email_builder("gmail.com") # ==> build_email("deveeswar") ==> deveeswar@gmail.com
ymail = email_builder("ymail.com")
hotmail = email_builder("hotmail.com")

print(gmail("deveeswar"))     # deveeswar@gmail.com
print(ymail("barath"))        # barath@ymail.com
print(hotmail("velmurugan"))  # velmurugan@hotmail.com


