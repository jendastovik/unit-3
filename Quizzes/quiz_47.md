# Quiz 47
## Python code
```python
from my_lib import DatabaseWorker
from my_lib import make_hash
from my_lib import check_hash

name = "bitcoin_exchange.db"
dat = DatabaseWorker(name)

query  = """SELECT * FROM ledger"""
res = dat.search(query, multiple=True)

dat.close()

total = 0
for row in res:
    id, sender_id, receiver_id, amount, hash = row 
    text = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"  
    check = check_hash(text, hash)
    if check:
        print(f"Tx(id={id})Signature matches")
    else:
        print(f"Tx(id={id})Error signature")

```

## Output
![](/Assets/q47.png)

## ER Diagram
![](/UML/bitcoin_exchange.png)
