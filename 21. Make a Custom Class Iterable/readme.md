🎯 Objective:
Aap ek Countdown class bana rahe hain jo kisi number se start kar ke 0 tak count kare reverse mein, aur use kiya ja sakay for loop mein.

🔍 Breakdown:
✅ __init__(self, start):
Yeh constructor hai, jisme user jo start number dega, woh self.start mein store hoga.

🔁 __iter__(self):
Is method ka kaam hota hai iterator object return karna.

Hum self.current ko initialize kar rahe hain jahan se countdown start hoga.

Yeh method self return karta hai, kyunke yahi object __next__() bhi define karta hai.

⏭ __next__(self):
Har baar jab loop chalega, yeh method call hoga.

Agar current < 0 ho gaya, to StopIteration raise hoga (loop ruk jaayega).

Warna current value return hogi, aur current -= 1 se agla number set hoga.

🧠 Important Concept:
Custom iterable banane ke liye aapko:

__iter__() method banana hota hai.

__next__() method banana hota hai.

StopIteration exception raise karna hota hai jab data khatam ho jaaye.

