class Order:
    def __init__(self, customer_name, items, total_amount, discount):
        self.customer_name = customer_name      # public
        self.items = items                      # public
        self.__total_amount = total_amount      # private
        self.__discount = discount              # private

    def __calculate_final(self): # private helper method
        return self.__total_amount - self.__discount

    def _get_admin_view(self): # protected method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Total Amount": f"₹{self.__total_amount}",
            "Discount Amount": f"₹{self.__discount}",
            "Final Amount": f"₹{self.__calculate_final()}"
        }

    def get_customer_view(self): # public method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Final Amount": f"₹{self.__calculate_final()}"
        }

class AdminPortal:
    def show_order(self, order):
        return order._get_admin_view() # ✅ allowed but protected

class CustomerApp:
    def show_order(self, order):
        return order.get_customer_view() # ✅ safe public method

order = Order("Devesh", ["Pizza", "Pepsi"], 600, 150)

admin = AdminPortal()
customer = CustomerApp()

print("👨🏻‍💼 Admin View:")        # 👨🏻‍💼 Admin View:
print(admin.show_order(order)) # {'Customer': 'Devesh', 'Items': ['Pizza', 'Pepsi'], 'Total Amount': '₹600', 'Discount Amount': '₹150', 'Final Amount': '₹450'}

print("\n🙍🏻‍♂️ Customer View:")      # 🙍🏻‍♂️ Customer View:
print(customer.show_order(order)) # {'Customer': 'Devesh', 'Items': ['Pizza', 'Pepsi'], 'Final Amount': '₹450'}
