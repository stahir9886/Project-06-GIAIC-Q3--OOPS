class Bank:
Humne ek class banayi jiska naam hai Bank.

bank_name = "Old Bank Name"
Ye ek class variable hai, jo har object ke liye common hota hai. Jaise static variable Java mein hota hai.

@classmethod decorator:
Ye batata hai ke method class level par kaam karega, na ke kisi specific object par.

def change_bank_name(cls, name):
Is method se hum class variable bank_name ko change kar sakte hain.
cls ka matlab hai class khud (jaise self hota hai instance ke liye).

account1 = Bank() aur account2 = Bank()
Do instances (objects) banaye hain bank ke.

Pehle bank_name print kiya:
Dono objects ka naam Old Bank Name tha.

Bank.change_bank_name("New Future Bank")
Class method se humne bank_name ko "New Future Bank" se update kiya.

Dubara print karne par dono ka naam change ho gaya:
Yeh prove karta hai ke class variable change hone se sabhi instances pe effect hota hai.