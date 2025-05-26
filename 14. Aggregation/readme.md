📘 Readme-style Explanation (Simple + Roman Urdu)
🧱 What is Aggregation?
Aggregation ek OOP relationship hai jahan ek class doosri class ka reference rakhti hai, lekin dono ka lifecycle alag hota hai.

🏢 Our Example:
Employee class mein employee ka naam store hota hai.

Department class ke constructor mein Employee ka reference pass hota hai.

Department sirf Employee object ko refer karta hai — uska malik nahi hota.

🔄 Proof of Aggregation:
Agar Department ka object delete ho bhi jaye, Employee ka object tab bhi kaam karega.

🧪 Output:
yaml
Copy
Edit
Department: IT | Employee Name: Ali Khan
Employee Name: Ali Khan
