# Access Modifiers in Python - Roman Urdu Explanation

## 🧠 Yeh Assignment Kya Hai?

Is assignment mein humne aik `Employee` class banai jisme teen variables hain:

1. `name` – yeh **public** variable hai.
2. `_salary` – yeh **protected** variable hai.
3. `__ssn` – yeh **private** variable hai.

## 🔎 Variables Access Karna

### 1. Public Variable:
- Isay object ke through **directly access** kar sakte hain.
- Example: `emp.name` se output mil jata hai.
- **Output**: Ali

### 2. Protected Variable:
- Isay bhi technically object se access kiya ja sakta hai, lekin yeh conventionally sirf class ya subclass ke andar use hota hai.
- Example: `emp._salary` se value mil jati hai.
- **Output**: 50000

### 3. Private Variable:
- Isay direct access karne par **error** aata hai.
- Example: `emp.__ssn` pe `AttributeError` milta hai.
- Isay access karne ka sahi tareeqa hota hai `emp._Employee__ssn` (name mangling ka use).

## ✅ Conclusion:
- Public: Fully accessible.
- Protected: Accessible but should be used with caution.
- Private: Not accessible directly, name mangling se access hota hai.

