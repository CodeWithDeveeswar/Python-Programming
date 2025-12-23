class dad:
    def house(self):
        print("Dad House")

class son1(dad):
    def factory(self):
        print("Son1 Factory")

class son2(dad):
    def market(self):
        print("Son2 Market")

g = son1()
g.house()   # Dad House
g.factory() # Son1 Factory

print()

v = son2()
v.house()  # Dad House
v.market() # Son2 Market