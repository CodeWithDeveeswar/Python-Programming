class grandfather:
     def car(self):
         print("Red Car")

class dad(grandfather):
    def house(self):
        print("House White")

class son(dad):
    def factory(self):
        print("Factory")

v = son()
v.house()   # House White
v.factory() # Factory
v.car()     # Red Car