def outer(msg):
    def inner():
        return f"Message is: {msg}"
    return inner

say_hi = outer("Vanakkam da mapla")

print(say_hi()) # Message is: Vanakkam da mapla