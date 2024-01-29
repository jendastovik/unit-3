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