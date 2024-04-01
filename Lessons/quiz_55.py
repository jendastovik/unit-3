class darts:
    def __init__(self) -> None:
        self.outer = 10
        self.middle = 5
        self.inner = 1
    
    def toss(self, x, y):
        cor = (x**2 + y**2)**0.5
        if cor > self.outer:
            return 0
        elif cor > self.middle:
            return 1
        elif cor > self.inner:
            return 5
        else:
            return 10
        
darts1 = darts()
print(f"toss at (0, 0): {darts1.toss(0, 0)}")
print(f"toss at (1, 1): {darts1.toss(1, 1)}")
print(f"toss at (5, 5): {darts1.toss(5, 5)}")
print(f"toss at (6, 6): {darts1.toss(6, 6)}")
print(f"toss at (10, 10): {darts1.toss(10, 10)}")
print(f"toss at (2, 3): {darts1.toss(2, 3)}")