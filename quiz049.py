from my_lib import DatabaseWorker

dat = DatabaseWorker("bitcoin_exchange.db")

dat.run_query("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
    )""")
# dat.insert("INSERT INTO users (id, name, email) VALUES ('920', 'bob6', 'dfj'), ('2', 'bob7', 'dfj'), ('3', 'bob8', 'dfj')")
query = """SELECT * FROM ledger join users on ledger.sender_id = users.id"""
query2 = """SELECT * FROM ledger join users on ledger.receiver_id = users.id"""
res = dat.search(query, multiple=True) + dat.search(query2, multiple=True)
print("\n".join([str(r) for r in res]))