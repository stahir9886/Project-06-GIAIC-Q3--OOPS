class MathUtils:
    # Static method for addition
    @staticmethod
    def add(a, b):
        return a + b

# Static method ko bina object banaye bhi call kar sakte hain
result = MathUtils.add(5, 10)
print("Sum is:", result)
