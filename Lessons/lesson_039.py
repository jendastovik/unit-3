from kivymd.app import MDApp

class my_first_app(MDApp):
    def build(self):
        return
    def pressed(self):
        label = self.root.ids.my_label
        button = self.root.ids.my_button
        label.text = "button pressed"
        label.color = "red"
        if button.md_bg_color == [0, 0, 1, 1]:
            button.md_bg_color = "red"
        else:
            button.md_bg_color = "blue"

text = my_first_app()
text.run()