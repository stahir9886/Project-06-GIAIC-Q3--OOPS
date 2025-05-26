class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# Create an object of Multiplier
times3 = Multiplier(3)

# Check if object is callable
print(callable(times3))  # Output: True

# Call the object like a function
result = times3(10)
print(result)  # Output: 30
