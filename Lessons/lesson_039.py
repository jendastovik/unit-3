from kivymd.app import MDApp

class my_first_app(MDApp):
    def build(self):
        return
    def pressed(self):
        label = self.root.ids.screen
        text = self.root.ids.my_label
        if label.md_bg_color == [1, 1, 1, 1]:
            label.md_bg_color = "black"
            text.color = "white"
        else:
            label.md_bg_color = "white"
            text.color = "black"

text = my_first_app()
text.run()