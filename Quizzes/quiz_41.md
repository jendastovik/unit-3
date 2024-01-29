# Quiz 41
## Python code
```python
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout

class tick(MDApp):
    def build(self):
        self.turn = 'X'
        return

    def press(self, btn):
        if self.turn=='X':
            btn.text = "X"
            btn.md_bg_color_disabled= "#D3A98A"
            btn.disabled = True
            self.root.ids.turn.text = "It is O's turn!"
            self.turn = 'O'
        else:
            btn.text = "O"
            btn.md_bg_color_disabled= "#90EE90"
            btn.disabled = True
            self.root.ids.turn.text = "It is X's turn!"
            self.turn = 'X'

test = tick()
test.run()
```

```kv
:kivy 1.0.9

Screen:
    size: 400,400

    MDBoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": 0.5,"center_y":0.5}
        size_hint: .7, .8

        MDLabel:
            size_hint: 1, .1
            halign: "center"
            text: "Tic Tac Toe by Jenda"
            font_size: "60px"
            bold: True

        MDLabel:
            id: turn
            size_hint: 1, .1
            halign: "center"
            text: "It is X's turn"
            font_size: "30px"
            bold: True

        MDBoxLayout:
            size_hint: 1,.8
            orientation: "vertical"
            spacing: 10
            MDBoxLayout:
                orientation: "horizontal"
                spacing: 20
                MDRectangleFlatButton:
                    id: btn1
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint: .3,1
                    on_release:
                        app.press(btn1)
                MDRectangleFlatButton:
                    id: btn2
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint:.3,1
                    on_release:
                        app.press(btn2)
                MDRectangleFlatButton:
                    id: btn3
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint:.3,1
                    on_release:
                        app.press(btn3)
            MDBoxLayout:
                orientation: "horizontal"
                spacing: 20
                MDRectangleFlatButton:
                    id: btn4
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint: .3,1
                    on_release:
                        app.press(btn4)
                MDRectangleFlatButton:
                    id: btn5
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint:.3,1
                    on_release:
                        app.press(btn5)
                MDRectangleFlatButton:
                    id: btn6
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint:.3,1
                    on_release:
                        app.press(btn6)
            MDBoxLayout:
                orientation: "horizontal"
                spacing: 20
                MDRectangleFlatButton:
                    id: btn7
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint: .3,1
                    on_release:
                        app.press(btn7)
                MDRectangleFlatButton:
                    id: btn8
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint:.3,1
                    on_release:
                        app.press(btn8)
                MDRectangleFlatButton:
                    id: btn9
                    text: ""
                    md_bg_color: "lightblue"
                    size_hint:.3,1
                    on_release:
                        app.press(btn9)
```

## Output
![](/Assets/q41.png)
### [video](https://drive.google.com/file/d/103HJWmEwkXQWPio_yAcEbEGVWtNFdFNI/view?usp=drive_link)

## UML diagram
![](/UML/q41.png)