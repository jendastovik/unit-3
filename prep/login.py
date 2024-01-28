from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


class LoginScreen(MDScreen):
    dialog=None

    def try_login(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        print(self.ids.uname.text)

    def register_btn(self):
        self.parent.current = "RegistrationScreen"


class RegistrationScreen(MDScreen):
    dialog = None
    def login_btn(self):
        self.parent.current = "LoginScreen"
    def try_register(self):
        email = self.ids.email.text
        pass1 = self.ids.pass1.text
        pass2 = self.ids.pass2.text
        uname = self.ids.uname.text
        
        if len(pass1)<8:
            self.ids.pass1.error=True
            self.ids.pass1.helper_text="Password must be at least 8 characters"
        elif pass1!=pass2:
            self.ids.pass2.error = True
            self.ids.pass2.helper_text="Password does not match. Try again."
        else:
            self.parent.current = "LoginScreen"

class login(MDApp):
    def build(self):
        Window.size = (500, 650)

app = login()
app.run()
