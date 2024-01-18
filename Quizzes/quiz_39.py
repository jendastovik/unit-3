from kivymd.app import MDApp

class quiz39(MDApp):
    def build(self):
        self.count = 0
        return
    def increment(self):
        label = self.root.ids.label
        button = self.root.ids.button
        self.count += 1
        label.text = "Count " + str(self.count)
    def substract(self):
        label = self.root.ids.label
        button = self.root.ids.button
        self.count -= 1
        label.text = "Count " + str(self.count)
        

text = quiz39()
text.run()
