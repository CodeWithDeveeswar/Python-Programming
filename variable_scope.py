# Variable scope defines where a variable can be accessed in a program

# Rule: L --> E --> G --> B

print() # New line
# ----------------------------------------------------------------------------------------------------------------------

# Local Variable scope
def order():
    food = "Curd rise"
    print("Your order is:", food)

order() # Your order is: Curd rise

# print(food) # NameError: name 'food' is not defined

print() # New line
# ----------------------------------------------------------------------------------------------------------------------

# Enclosing Variable scope
def cart():
    discount = 10

    def checkout():
        print("Applying discount:", discount)

    checkout()

cart() # Applying discount: 10

print() # New line
# ----------------------------------------------------------------------------------------------------------------------

# Global Variable scope
user_id = "deveeswar2002"

def homepage():
    print("Welcome:", user_id)

def profile():
    print("Welcome to the profile page:", user_id)

homepage() # Welcome: deveeswar2002

profile() # Welcome to the profile page: deveeswar2002

print() # New line
# ----------------------------------------------------------------------------------------------------------------------

# Built-in Variable scope
print(__file__) # E:\Python\Python Programming\variable_scope.py

print(len("deveeswar2002")) # 13

print() # New line
# ----------------------------------------------------------------------------------------------------------------------

# Swiggy Use Case
delivery_partner = "Swiggy" # Global Variable scope

def hotel():
    item = "Pizza" # Local Variable scope

    def order_now():
        quantity = 2 # Enclosing Variable scope
        print(f"Ordering {quantity} {item} using {delivery_partner}")

    order_now()

hotel() # Ordering 2 Pizza using Swiggy

