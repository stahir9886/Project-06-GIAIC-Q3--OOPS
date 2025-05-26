class Counter:
    count = 0  # Class variable to track the number of objects
    
    @classmethod
    def increment_count(cls):
        cls.count += 1  # Increase the object count by 1
    
    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

# Creating first object
obj1 = Counter()
obj1.increment_count()  # count becomes 1

# Creating second object
obj2 = Counter()
obj2.increment_count()  # count becomes 2

# Creating third object
obj3 = Counter()
obj3.increment_count()  # count becomes 3

# Display the number of objects created
Counter.display_count()  # Output: Number of objects created: 3
