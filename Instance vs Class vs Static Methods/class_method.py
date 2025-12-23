class Employee:
    company_name = "OpenAI" # Class-level data

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

Employee.change_company("Google")
print(Employee.company_name) # Output: Google