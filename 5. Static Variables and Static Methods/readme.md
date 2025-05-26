class MathUtils:
Humne ek class banayi jiska naam hai MathUtils.

@staticmethod decorator:
Iska matlab hai ke ye method kisi bhi instance (self) ya class (cls) se related nahi hai.
Sirf input values (parameters) le kar kaam karega.

def add(a, b):
Ye method do numbers lega aur unka sum return karega. Simple mathematical logic hai.

MathUtils.add(5, 10)
Static method ko class ke naam se direct call kiya ja sakta hai — object banane ki zarurat nahi.

Output:
print("Sum is:", result) se output aayega:
Sum is: 15