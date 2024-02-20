from my_lib import DatabaseWorker
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp

class dropList(MDApp):
    def build(self):
        self.x = DatabaseWorker("bitcoin_exchange.db")
        query = """SELECT * FROM users"""
        self.users = self.x.search(query, multiple=True)
        Window.size = (500, 700)
        self.x.close()

    def open_menu(self, drop_item_element):
        self.menu_items = [c[1] for c in self.users]
        buttons_menu =[]
        for item in self.menu_items:
            buttons_menu.append(
                {"text": item, 
                 "on_release": lambda x = item: self.button_pressed(x),
                 "viewclass": "OneLineListItem",
                 }
            )
        self.menu = MDDropdownMenu(caller=drop_item_element, items=buttons_menu, width_mult=2)
        self.menu.open()
    def button_pressed(self, x):
        user = self.x.search(f"SELECT * FROM users WHERE name = '{x}'")
        if user:
            self.root.ids.customer.text = f"customer {user[1]} with id {user[0]}"
            self.root.ids.dropdown_user.text = user[1]
        self.menu.dismiss()

test = dropList()
test.run()
        

        
