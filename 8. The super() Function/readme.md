# The super() Function - Roman Urdu Explanation

## 👨‍🏫 Assignment Ka Maksad:
Yeh assignment inheritance ka concept samjhanay ke liye hai jisme aik base class `Person` banani hai, aur us se derived class `Teacher` banani hai. `super()` function ka use kar ke base class ka constructor call karna hai.

---

## 📘 Step by Step Explanation:

### 1. Person Class (Base Class):
- Is class mein aik `__init__` constructor hai jo `name` ko set karta hai.
- Example: `self.name = name`

### 2. Teacher Class (Derived Class):
- Is class ne `Person` class se inherit kiya hai.
- Ismein aik extra field `subject` hai.
- Humne `super().__init__(name)` ka use kiya hai taake base class ka constructor call ho jaye aur `name` set ho jaye.

### 3. Object Creation:
- Jab hum `Teacher("Ali", "Math")` call karte hain:
  - Pehle `Person` class ka constructor `super()` ke zariye call hota hai aur name set hota hai.
  - Phir `subject` set hota hai.

### 4. Output:
- `teacher.name` → "Ali"
- `teacher.subject` → "Math"

---

## ✅ Conclusion:
- `super()` ka use base class ke methods ya constructor ko access karne ke liye hota hai.
- Is se hum code reuse kar sakte hain aur maintain karna asaan hota hai.
- Inheritance ka yeh powerful feature hai object-oriented programming mein.

