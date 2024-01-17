class CompoundInterest:
    def __init__(self, principal, rate, num_of_years):
        self.principal = principal
        self.rate = rate
        self.time = num_of_years

    def calculate(self):
        return self.principal * (1 + self.rate) ** self.time
    
class Accounting(CompoundInterest):
    def __init__(self, holder_name, holder_email, principal, rate, num_of_years):
        super().__init__(principal, rate, num_of_years)
        self.holder_name = holder_name
        self.holder_email = holder_email
    
    def get_msg(self):
        return f"{self.holder_name} will have {self.calculate():,.2f}USD in {self.time} years if the principal is {self.principal:,} with {self.rate}% anual compound interest."
        
john = Accounting("John", "dkj", 1000000, 0.05, 10)

print(john.get_msg())
