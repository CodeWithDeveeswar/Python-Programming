class Employee:
    def __init__(self, name, aadhaar):
        self.name = name         # Stored once
        self.aadhaar = aadhaar   # Stored once

    def enter_office(self):
        print(f"{self.name} enters using Aadhaar {self.aadhaar}.")

    def open_bank_account(self):
        print(f"Bank account opened for {self.name} with {self.aadhaar}.")

emp1 = Employee("Deveeswar", "1234-5678-9101")
emp1.enter_office()      # Deveeswar enters using Aadhaar 1234-5678-9101.
emp1.open_bank_account() # Bank account opened for Deveeswar with 1234-5678-9101.