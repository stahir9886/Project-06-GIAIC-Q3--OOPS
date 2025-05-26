class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn          # Private variable

# Object create karte hain
emp = Employee("Ali", 50000, "123-45-6789")

# Public variable access
print("Name (Public):", emp.name)

# Protected variable access
print("Salary (Protected):", emp._salary)

# Private variable access - direct access se error hoga
try:
    print("SSN (Private):", emp.__ssn)
except AttributeError as e:
    print("Private access error:", e)

# Private variable ko access karne ka sahi tarika (name mangling)
print("SSN (Private via name mangling):", emp._Employee__ssn)
