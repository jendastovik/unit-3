# Quiz 45
## Python code
```python
from my_lib import DatabaseWorker

haiku = """Code flows like a stream
alghorithms guide its way
in silence, it solves"""

db_name = "database_test.db"
db = DatabaseWorker(db_name)

db.run_query("DROP TABLE IF EXISTS Words")

query = """CREATE TABLE IF NOT EXISTS Words (
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL,
    length INTEGER NOT NULL
    )"""
db.run_query(query=query)

for word in haiku.split():
    query = f"""INSERT INTO Words (word, length) VALUES ('{word}', {len(word)})"""
    db.insert(query)

# query the average of all the leghts of the words
query = "SELECT AVG(length) FROM Words"
out = db.search(query, multiple=False)[0]
print(f"The average word lenght is {out:.2f}")

db.close()
```

## Output
![](/assets/q45.png)


