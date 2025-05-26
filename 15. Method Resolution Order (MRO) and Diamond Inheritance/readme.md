 Readme-style Explanation (Roman Urdu + Simple English)
🧱 MRO (Method Resolution Order) kya hota hai?
MRO decide karta hai ke jab kisi method ko call karna ho multiple inherited classes mein, to Python kis class ka method pehle chalaye. Ye left-to-right hota hai by default (in case of class D(B, C)).

🔷 Diamond Inheritance Structure:
css
Copy
Edit
    A
   / \
  B   C
   \ /
    D
Yani B aur C dono A se inherit karte hain, aur D in dono se.

🔁 Jab obj.show() call hota hai:
Python left-to-right check karta hai: D -> B -> C -> A

B mein show() mila, to wahi run hua.

🔎 MRO Dekhne ka Tarika:
python
Copy
Edit
print(D.__mro__)
Yeh line aapko exact order dikhati hai jisme Python method dhoondta hai.

