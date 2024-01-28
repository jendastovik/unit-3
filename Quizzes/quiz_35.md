# Quiz 35
## Python code
```python
class Account:
    def __init__(self, balance = 0, holder_name = "", holder_email = "", number = ["000", "00000", "0"]):
        self.balance = balance
        self.holder_name = holder_name
        self.holder_email = holder_email
        self.number = number
    
    def get_account_no(self):
        return "-".join(self.number)
    
    def set_holder_name(self, name: str):
        self.holder_name = name
        return f"Holder's name set to {self.holder_name}"
    
    def get_balance(self):
        return self.balance
    
    def set_holder_email(self, email: str):
        if "@" not in email or email.count("@") > 1:
            raise ValueError("Invalid email")
        self.holder_email = email
        return f"Holder's email set to {self.holder_email}"
    
    def deposit(self, amount: int):
        self.balance += amount
        return f"New balance: {self.balance} USD"
```

## Output
![](/Assets/q35.png)