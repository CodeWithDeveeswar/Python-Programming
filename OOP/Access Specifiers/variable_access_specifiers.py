class Parent:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

    def access_from_same_class(self):
        print("Inside Parent Class:")
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        print("Private:", self.__private_var)

class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child Class (Subclass):")
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        try:
            print("Private:", self.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot Access (AttributeError)")

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger Class (Unrelated):")
        print("Public:", obj.public_var)
        print("Protected:", obj._protected_var) # ⚠️ Not Recommended
        try:
            print("Private:", obj.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot Access (AttributeError)")

# Demo
p = Parent()
c = Child()
s = Stranger()

print("\n➡️ Access from SAME CLASS:")
p.access_from_same_class() # ➡️ Access from SAME CLASS:
                           # Inside Parent Class:
                           # Public: I am Public
                           # Protected: I am Protected
                           # Private: I am Private

print("\n➡️ Access from SUBCLASS:")
c.access_from_subclass() # ➡️ Access from SUBCLASS:
                         # Inside Child Class (Subclass):
                         # Public: I am Public
                         # Protected: I am Protected
                         # Private: ❌ Cannot Access (AttributeError)

print("\n➡️ Access from OTHER CLASS:")
s.access_from_other_class(p) # ➡️ Access from OTHER CLASS:
                             # Inside Stranger Class (Unrelated):
                             # Public: I am Public
                             # Protected: I am Protected
                             # Private: ❌ Cannot Access (AttributeError)

