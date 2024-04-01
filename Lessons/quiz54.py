class rainDrops:
    def pour(self, n:int):
        d = {3: "Pling", 5: "Plang", 7: "Plong"}
        out = ""
        for k, v in d.items():
            out += (n%k == 0) * v

        out += (out == "") * str(n)
        return out
    def pour2(self, n:int):
        d = [(3, "i"), (5, "a"), (7, "o")]
        out = [f"Pl{r}ng"*(n%k == 0) for k, r in d]
        return "".join(out) or str(n)
    
rain = rainDrops()
print(rain.pour2(28))
print(rain.pour2(30))
print(rain.pour2(34))
