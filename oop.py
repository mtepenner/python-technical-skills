class Employee:
    # __init__ is a dunder method for initialization
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # Single underscore implies private/internal use

    # __str__ defines how the object is printed
    def __str__(self):
        return f"{self.name} earns ${self._salary}"

# Inheritance
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary) # Call parent class constructor
        self.department = department

    def __str__(self):
        return f"{self.name} manages {self.department}"

boss = Manager("Alice", 120000, "Engineering")
print(boss) # Outputs: Alice manages Engineering
