from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Object creation
rect = Rectangle(5, 10)
print("Rectangle Area:", rect.area())
