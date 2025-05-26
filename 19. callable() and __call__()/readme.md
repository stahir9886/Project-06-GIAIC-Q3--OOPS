🎯 __call__() kya karta hai?
Jab aap kisi object ko function ki tarah likhte hain — jaise obj(10) — to Python actually obj.__call__(10) run karta hai.

🔁 Multiplier class ka kya kaam hai?
Jab object banta hai (Multiplier(3)), to factor set hota hai.

Jab object function ki tarah call hota hai (times3(10)), to woh 10 ko 3 se multiply karta hai.

🔍 callable(times3) kya check karta hai?
Ye check karta hai ke object ko function ki tarah call kiya ja sakta hai ya nahi.

Agar class ne __call__() method define kiya ho, to object callable hota hai.

🧪 Output:
graphql
Copy
Edit
True
30
