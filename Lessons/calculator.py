from kivymd.app import MDApp

class calculator(MDApp):
    def build(self):
        self.res = 0
        self.num = ""
        self.numbers = []
        self.operations=[]
        return
    def number_pressed(self, num):
        if self.res == 0 and self.num == "":
            self.root.ids.label.text = ""
        label = self.root.ids.label
        label.text += str(num)
        self.num += str(num)
    def operation_pressed(self, operation):
        if self.num == "" and len(self.numbers) == 0:
            self.num = self.root.ids.label.text
        elif self.num == "":
            return
        self.operations.append(operation)
        self.numbers.append(self.num)
        self.root.ids.label.text = ""
        self.num = ""
    def add(self, num):
        self.res += float(num)
    def subtract(self, num):
        self.res -= float(num)
    def multiply(self, num):
        self.res *= float(num)
    def devide(self, num):
        self.res /= float(num)

    def evaluate(self):
        self.numbers.append(self.num)
        self.res = float(self.numbers[0])
        for N in range(len(self.operations)):
            if self.operations[N] == "+":
                self.add(self.numbers[N+1])
            elif self.operations[N] == "-":
                self.subtract(self.numbers[N+1])
            elif self.operations[N] == "*":
                self.multiply(self.numbers[N+1])
            elif self.operations[N] == "/":
                self.devide(self.numbers[N+1])
        self.root.ids.label.text = str(self.res)
        self.num = ""
        self.operations = []
        self.numbers = []
        self.res = 0
    def decimal_pressed(self):
        label = self.root.ids.label
        label.text += "."
        self.num += "."
    def clear(self):
        self.num = ""
        self.numbers = []
        self.root.ids.label.text = ""
    def toggle_sign(self):
        label = self.root.ids.label
        txt = label.text
        if txt == "":
            label.text = "-"
        elif txt[0] == "-":
            label.text = txt[1:]
        else:
            label.text = "-" + txt
        self.num = label.text
    def calculate_percentage(self):
        label = self.root.ids.label
        label.text = str(float(label.text)/100)
        self.num = label.text
    
text = calculator()
text.run()