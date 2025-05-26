class Logger:
    # Constructor: Jab object create hota hai
    def __init__(self):
        print("Logger object created!")

    # Destructor: Jab object destroy hota hai
    def __del__(self):
        print("Logger object destroyed!")

# Object bana rahe hain
log = Logger()

# Object ko manually delete karte hain (optional)
del log

# Note: destructor automatically call hota hai jab object destroy hota hai,
# ya program end hota hai
