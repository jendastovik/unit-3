# Quiz 38
## Python code
```python
import random
import matplotlib.pyplot as plt

class SalemanMap:
    def __init__(self) -> None:
        self.x = []
        self.y = []
        self.name = []
    
    def generate_data(self, names: list):
        for name in names:
            self.name.append(name)
            self.x.append(random.randint(0, 100))
            self.y.append(random.randint(0, 100))
    def get_map(self):
        for i in range(len(self.name)):
            plt.scatter(self.x[i], self.y[i], label=self.name[i], color='red')
            plt.text(self.x[i], self.y[i], self.name[i], fontsize=10, ha="left" )
        plt.ylabel("Distance (km)")
        plt.xlabel("Distance (km)")
        #plt.yticks([20, 30, 40, 50, 60, 70, 80, 90, 100])
        plt.show()

test = SalemanMap()
test.generate_data(["kobe", "Tokyo", "Osaka", "Nagoya", "Fukuoka", "Sapporo", "Sendai", "Kumamoto", "Naha"])
test.get_map()
```

## Output
![](/assets/q38.png)