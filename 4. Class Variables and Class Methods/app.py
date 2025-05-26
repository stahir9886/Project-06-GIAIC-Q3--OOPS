class Bank:
    # Class variable (ye sab objects ke liye common hota hai)
    bank_name = "Old Bank Name"

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # cls se class variable access hota hai

# Pehle kuch objects banate hain
account1 = Bank()
account2 = Bank()

# Dono accounts ka bank_name print karte hain
print("Before changing:")
print("Account 1 bank:", account1.bank_name)
print("Account 2 bank:", account2.bank_name)

# Ab bank name change karte hain using class method
Bank.change_bank_name("New Future Bank")

# Phir se check karte hain kya dono pe effect aaya?
print("\nAfter changing:")
print("Account 1 bank:", account1.bank_name)
print("Account 2 bank:", account2.bank_name)
