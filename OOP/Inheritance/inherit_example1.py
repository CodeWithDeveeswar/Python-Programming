from inherit_example2 import dad

class son(dad):
    def factory(self):
        print("White")

    def house(self):
        print("Yellow")

s = son()
s.house()   # Yellow
s.factory() # White