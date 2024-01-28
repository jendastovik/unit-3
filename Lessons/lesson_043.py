from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp


class MyButton(MDBoxLayout):
    pass

class Game(MDApp):
    def build(self):
        Window.size = (400, 600)
    def buttonPressed(self):
        print("Button pressed")

g = Game()
g.run()