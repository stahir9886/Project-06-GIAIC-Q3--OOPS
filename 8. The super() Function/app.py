# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Base class ka constructor call
        self.subject = subject

# Object create karna
teacher = Teacher("Ali", "Math")

# Output print karna
print("Name:", teacher.name)
print("Subject:", teacher.subject)
