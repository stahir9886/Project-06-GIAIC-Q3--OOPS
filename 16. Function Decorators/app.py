# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Function to decorate
@log_function_call
def say_hello():
    print("Hello, world!")

# Call the function
say_hello()
