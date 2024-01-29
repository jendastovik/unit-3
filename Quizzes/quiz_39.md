# Quiz 39
## Python code
```python
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
```

```kivymd
#:kivy 1.0.9

Screen:
    size: 500, 500

    BoxLayout:
        orientation: 'horizontal'
        size_hint: .7, .3
        pos_hint: {'center_x': .5, 'center_y': .5}

        MDRaisedButton:
            size_hint: .3, 1
            text: 'sub -1'
            font_size: 34
            md_bg_color: "black"
            on_press: app.substract()

        MDLabel:
            id: label
            size_hint: .3, 1
            text: 'Count 0'
            font_size: 34
            md_bg_color: "#ADD8E6"
            halign: 'center'
            color: "red"
            
        MDRaisedButton:
            id: button
            size_hint: .3, 1
            text: 'Add +1'
            font_size: 34
            md_bg_color: "black"
            on_press: app.increment()

```

## Output
![](/Assets/q39.png)

