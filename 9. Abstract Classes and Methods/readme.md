# Abstract Classes and Methods - Roman Urdu Explanation

## 🎯 Assignment Ka Maksad:
Is assignment ka goal yeh hai ke hum `abc` module ka use karke aik abstract class banayein aur phir usay inherit kar ke concrete class mein method implement karein.

---

## ⚙️ Step by Step Code Samjhaani:

### 1. `from abc import ABC, abstractmethod`
- Yeh `abc` module import karta hai.
- `ABC` ka matlab hai **Abstract Base Class**.
- `abstractmethod` decorator se method ko abstract banate hain (i.e. bina body ke).

---

### 2. Shape Class (Abstract Class):
```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
