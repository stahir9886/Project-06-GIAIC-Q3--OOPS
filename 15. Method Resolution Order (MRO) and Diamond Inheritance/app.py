class A:
    def show(self):
        print("Show from Class A")

class B(A):
    def show(self):
        print("Show from Class B")

class C(A):
    def show(self):
        print("Show from Class C")

class D(B, C):  # Diamond Inheritance
    pass

# Creating object of class D
obj = D()
obj.show()

# Let's also print MRO
print(D.__mro__)
