# Quiz 37
## Python code
```python
class CompoundInterest:
    def __init__(self, principal = 0, rate = 0, num_of_years = 0):
        self.principal = principal
        self.rate = rate
        self.time = num_of_years

    def calculate_interest(self):
        res = self.principal * (1 + self.rate) ** self.time
        return float(format(res, ".2f"))
    
    def set_principal(self, principal):
        if principal <= 0:
            raise ValueError("Principal should be greater than zero")
        self.principal = principal
    
    def set_rate(self, rate):
        if rate <= 0:
            raise ValueError("Interest rate should be greater than zero")
        self.rate = rate
    
    def set_years(self, years):
        if years <= 0:
            raise ValueError("Years should be greater than zero")
        self.time = years

    
class AccountingProgram(CompoundInterest):
    def __init__(self, holder_name = "", holder_email = "", principal = 0, rate = 0, num_of_years = 0):
        super().__init__(principal, rate, num_of_years)
        self.holder_name = holder_name
        self.holder_email = holder_email
    
    def get_msg(self):
        return f"{self.holder_name} will have {self.calculate():,.2f}USD in {self.time} years if the principal is {self.principal:,} with {self.rate}% anual compound interest."
        
```

## Output
![](/assets/q37.png)

## UML diagram