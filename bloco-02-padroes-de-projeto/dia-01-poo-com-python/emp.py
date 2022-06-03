class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Objects of class Emp has been made here
Emps = [Emp("John", 25), Emp("Mary", 30), Emp("Peter", 35)]

# Objects of class Emp has been used here
for emp in Emps:
    emp.info()