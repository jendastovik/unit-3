# Quiz 49
## Python code
```python
from my_lib import DatabaseWorker

dat = DatabaseWorker("bitcoin_exchange.db")

dat.run_query("DROP TABLE IF EXISTS users")

dat.run_query("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
    )""")

# selects all unique ids from the ledger
ids_in_ledger = dat.search("SELECT sender_id FROM ledger", multiple=True) + dat.search("SELECT receiver_id FROM ledger", multiple=True)
unique_ids_in_ledger = [i[0] for i in list(set(ids_in_ledger))]

# inserts a user for each unique id in the ledger
for i in unique_ids_in_ledger:
    dat.run_query(f"INSERT INTO users (id, name, email) VALUES ({i}, 'bob{i-914}', 'bob{i}@bobis.com')")

# selects all transactions with bob6 as a sender or a receiver
query = """SELECT ledger.* FROM ledger join users on ledger.sender_id = users.id WHERE users.name = 'bob6'"""
query2 = """SELECT ledger.* FROM ledger join users on ledger.receiver_id = users.id WHERE users.name = 'bob6'"""
res = dat.search(query, multiple=True) + dat.search(query2, multiple=True)
print("\n".join([str(r) for r in res]))
```

## Output
![](/Assets/q49.png)
![](/Assets/q49B.png)

## ER Diagram
![](/UML/bitcoin_exchange.png)

