# Quiz 54
## Python code
```python
class rainDrops:
    def pour(self, n:int):
        d = {3: "Pling", 5: "Plang", 7: "Plong"}
        out = ""
        for k, v in d.items():
            out += (n%k == 0) * v

        out += (out == "") * str(n)
        return out
    
rain = rainDrops()
print(rain.pour(28))
print(rain.pour(30))
print(rain.pour(34))
```

## Output
![](/Assets/q54.png)