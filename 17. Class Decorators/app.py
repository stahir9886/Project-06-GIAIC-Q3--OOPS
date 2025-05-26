# Class decorator function
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add greet method dynamically to the class
    return cls

# Apply decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create object and call the added method
p = Person("Ramesha")
print(p.greet())
