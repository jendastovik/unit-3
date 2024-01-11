class Account:
    def __init__(self, balance = 0, holder_name = "", holder_email = "", number = ["000", "00000", "0"]):
        self.balance = balance
        self.holder_name = holder_name
        self.holder_email = holder_email
        self.number = number
    
    def get_account_number(self):
        return "-".join(self.number)
    
    def set_holder_name(self, name):
        self.holder_name = name
        return f"Holder's name is {self.holder_name}"
    
    def get_balance(self):
        return self.balance
    
    def set_holder_email(self, email):
        self.holder_email = email
        return f"Holder's email is {self.holder_email}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"New balance: {self.balance}USD"
    

