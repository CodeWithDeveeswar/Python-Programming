class dad:
    def house(self):
        print("Dad's House")

class mom:
    def shop(self):
        print("Mom's Shop")

class daughter(dad, mom):
    def factory(self):
        print("Daughter's Factory")

d = daughter()
d.shop()    # Mom's Shop
d.house()   # Dad's House
d.factory() # Daughter's Factory