class Dog:
    def __init__(self, name, breed):
        self.name = name        # Instance variable for dog's name
        self.breed = breed      # Instance variable for dog's breed

    def bark(self):
        print(f"{self.name} is barking! Woof woof!")  # Instance method that uses self.name


# Object create karte hain:
dog1 = Dog("Tommy", "German Shepherd")

# Method call karte hain:
dog1.bark()
