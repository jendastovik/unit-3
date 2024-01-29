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