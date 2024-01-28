from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

class MysteryPageA(MDScreen):
    def try_change(self):
        self.parent.current = "MysteryPageB"

class MysteryPageB(MDScreen):
    def try_change(self):
        self.parent.current = "MysteryPageA"
    

class Quiz42(MDApp):
    def build(self):
        Window.size = (300, 500)




t = Quiz42()
t.run()