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