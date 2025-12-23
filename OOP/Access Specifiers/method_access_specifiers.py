class Parent:
    def public_method(self):
        print("Public Method")

    def _protected_method(self):
        print("Protected Method")

    def __private_method(self):
        print("Private Method")

    def access_from_same_class(self):
        print("Inside Parent Class:")
        self.public_method()
        self._protected_method()
        self.__private_method()

class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child Class (Subclass):")
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
        except AttributeError:
            print("Private method: ❌ Cannot Access (AttributeError)")

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger Class (Unrelated):")
        obj.public_method()
        obj._protected_method() # ⚠️ Not Recommended
        try:
            obj.__private_method()
        except AttributeError:
            print("Private method: ❌ Cannot Access (AttributeError)")

# Demo
p = Parent()
c = Child()
s = Stranger()

print("\n➡️ Access from SAME CLASS:")
p.access_from_same_class() # ➡️ Access from SAME CLASS:
                           # Inside Parent Class:
                           # Public Method
                           # Protected Method
                           # Private Method

print("\n➡️ Access from SUBCLASS:")
c.access_from_subclass() # c.access_from_subclass()
                         # ➡️ Access from SUBCLASS:
                         # Inside Child Class (Subclass):
                         # Public Method
                         # Protected Method
                         # Private method: ❌ Cannot Access (AttributeError)

print("\n➡️ Access from OTHER CLASS:")
s.access_from_other_class(p) # ➡️ Access from OTHER CLASS:
                             # Inside Stranger Class (Unrelated):
                             # Public Method
                             # Protected Method
                             # Private method: ❌ Cannot Access (AttributeError)





