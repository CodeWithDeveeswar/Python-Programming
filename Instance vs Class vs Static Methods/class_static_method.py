class Employee:
    company_name = "OpenAI" # Class-level data

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name # Accessing class variable

    @staticmethod
    def try_change_company(new_name):
        company = new_name

# Call both methods
Employee.change_company("Google")
print("After Classmethod:", Employee.company_name)  # After Classmethod: Google

Employee.try_change_company("Meta")
print("After Staticmethod:", Employee.company_name) # After Staticmethod: Google