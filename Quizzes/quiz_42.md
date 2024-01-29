# Quiz 42
## Python code
```python
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen


class Mystery(MDApp):
    def build(self):
        return
    
class MysteryPageA(MDScreen):

    def message1(self):
        print("This is mystery page A you pressed the button")

class MysteryPageB(MDScreen):

    def message2(self):
        print("This is mystery page B you pressed the button")

t = Mystery()
t.run()
```

```kv
#:kivy 1.0.9
#:kivy 1.0.9

ScreenManager:
    MysteryPageA: 
        name:"a"
    MysteryPageB: 
        name:"b"

<MysteryPageA>:
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        MDLabel:
            text: "MysteryPageA"
            font_style: 'H2'
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            halign: 'center'
        MDRaisedButton:
            text: 'Go to second screen'
            pos_hint: {'left': 0, 'bottom': 0}
            md_bg_color: "blue"
            on_release: 
                root.parent.current = 'b'
                root.parent.get_screen('b').message2()

            

<MysteryPageB>:
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        md_bg_color: "black"
        MDLabel:
            text: "MysteryPageB"
            font_style: 'H2'
            color: "white"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            halign: 'center'
        MDRaisedButton:
            text: 'Go to first screen'
            pos_hint: {'left': 0, 'bottom': 0}
            md_bg_color: "blue"
            on_release: 
                root.parent.current = 'a'
                root.parent.get_screen('a').message1()
```

## Output
![](/assets/q42A.png)
![](/assets/q42B.png)