# Method Overriding
class dad:
    def house(self):
        print("House White")

class daughter(dad):
    def factory(self):
        print("Factory")

    def house(self):
        print("House Yellow")

d = daughter()
d.house()   # House Yellow
d.factory() # Factory

# Note: There is such a concept of OverLoading in Python Polymorphism