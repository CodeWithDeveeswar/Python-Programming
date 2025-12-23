class dad:
    def house(self):
        print("I am from dad class")

class son(dad):
    def factory(self):
        print("I am from son class")

s = son()
s.house()   # I am from dad class
s.factory() # I am from son class

print()

# Use Case 1: Method Overriding
class Dad:
    def house(self):
        print("Red")

class Son(Dad):
    def factory(self):
        print("White")

    def house(self):
        print("Yellow")

a = Son()
a.house()   # Yellow
a.factory() # White






