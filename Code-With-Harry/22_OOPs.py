# Object Oriented Programming

# Note : "this" in JavaScript is "self" in python
class Employee:
    # Constructor function : Method which runs automatically when a new object is created everytime.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return f"The salary of {self.name} is {self.salary}!!"
    
emp1 = Employee("Amith", 100000)
print(emp1.getSalary())

emp2 = Employee("Varun", 125000)
print(emp2.getSalary())