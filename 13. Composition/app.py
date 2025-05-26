# engine.py

class Engine:
    def start(self):
        return "Engine started successfully!"

# car.py

from engine import Engine  # type: ignore # If files are separate, use this. Else define in same file.

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine method through Car

# main.py (or directly run this section)

if __name__ == "__main__":
    engine_obj = Engine()            # Creating Engine object
    car_obj = Car(engine_obj)        # Passing Engine to Car (Composition)
    
    print(car_obj.start_car())       # Output: Engine started successfully!
