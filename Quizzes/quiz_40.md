# Quiz 40
## Python code
```python
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

class FirstScreen(MDScreen):
    def try_change(self):
        self.parent.current = "second"

class SecondScreen(MDScreen):
    pass
    

class MultipleScreen(MDApp):
    def build(self):
        Window.size = (300, 500)


t = MultipleScreen()
t.run()
```

```.kv
#:kivy 1.0.9

ScreenManager:
    FirstScreen: 
        name:"first"
    SecondScreen: 
        name:"second"

<firstScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        MDLabel:
            text: "Jenda's First Screen"
            font_style: 'H2'
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            halign: 'center'
        MDRaisedButton:
            text: 'Go to second screen'
            pos_hint: {'left': 0, 'bottom': 0}
            md_bg_color: "blue"
            on_release: root.try_change()
            

<secondScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        md_bg_color: "black"
        MDLabel:
            text: "Jenda's Second Screen"
            font_style: 'H2'
            color: "white"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            halign: 'center'
        MDRaisedButton:
            text: 'Go to first screen'
            pos_hint: {'left': 0, 'bottom': 0}
            md_bg_color: "blue"
            on_release: root.parent.current = 'first'
```

## Output
![](/Assets/q40A.png)
![](/Assets/q40B.png)

## UML diagram
![](/UML/q40.png)