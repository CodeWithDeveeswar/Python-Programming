from abc import ABC, abstractmethod

# Architect defines the plan
class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

# Developer implements it
class WepApp(FeaturePlan):
    def login(self):
        print("WebApp Login Done ✅")

    def logout(self):
        print("WebApp Logout Done ✅")

# Team lead checks functionality
app = WepApp()
app.login()  # WebApp Login Done ✅
app.logout() # WebApp Logout Done ✅