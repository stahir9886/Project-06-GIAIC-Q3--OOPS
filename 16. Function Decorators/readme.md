🎯 Decorator kya hota hai?
Decorator ek special function hota hai jo kisi doosre function ke behavior ko modify ya enhance karta hai bina uska code directly change kiye.

📦 @log_function_call kya karta hai?
Yeh Python ka shorthand hai jo kehta hai:

python
Copy
Edit
say_hello = log_function_call(say_hello)
🔄 Jab say_hello() call hota hai:
Pehle log_function_call ka wrapper() function run hota hai.

Pehle print karta hai "Function is being called".

Phir original say_hello() ko call karta hai.