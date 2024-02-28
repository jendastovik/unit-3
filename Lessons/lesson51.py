from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from my_lib import DatabaseWorker
from my_lib import make_hash

class TableScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables= None
        self.selected_rows = []
    
    def on_pre_enter(self, *args):
        column_names= [("id", 40), ("Sender", 30), ("Receiver", 30), ("Amount", 40), ("Signature", 100)]
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=True,
            check=True,
            column_data=column_names
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = lesson51.x.search("""SELECT * FROM ledger""", multiple=True)
        print(data)
        self.data_tables.update_row_data(None, data)
    
    def row_pressed(self, instance_table, instance_row):
        pass
    
    def checkbox_pressed(self, instance_table, current_row):
        if current_row in self.selected_rows:
            self.selected_rows.remove(current_row)
        else:
            self.selected_rows.append(current_row)
        print(self.selected_rows)

    def save(self):
        sender = self.ids.sender.text
        receiver = self.ids.receiver.text
        amount = self.ids.amount.text
        signature = f"sender_id {sender}, receiver_id {receiver}, amount {amount}"
        print(sender, receiver, amount)
        save_query = f"""INSERT INTO ledger (sender_id, receiver_id, amount, signature) VALUES ({sender}, {receiver}, {amount}, '{make_hash(signature)}')"""
        lesson51.x.insert(save_query)
        self.update()



class lesson51(MDApp):
    x =DatabaseWorker('bitcoin_exchange.db')
    def build(self):
        pass

test = lesson51()
test.run()
lesson51().x.close()