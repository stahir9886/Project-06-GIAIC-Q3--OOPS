# Class banayi jiska naam hai Car
class Car:
    # Public variable brand
    def __init__(self, brand):
        self.brand = brand

    # Public method start
    def start(self):
        print(f"{self.brand} car is starting...")

# Class ka object banaya
my_car = Car("Toyota")

# Public variable ko access kiya
print("Car brand:", my_car.brand)

# Public method ko call kiya
my_car.start()
