class Student:
    # Constructor
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} is in grade {self.grade}")

# Multiple Objects
s1 = Student("Deveeswar", 10)
s2 = Student("Aishwarya", 12)
s3 = Student("Akilan", 11)

s1.display() # Deveeswar is in grade 10
s2.display() # Aishwarya is in grade 12
s3.display() # Akilan is in grade 11
