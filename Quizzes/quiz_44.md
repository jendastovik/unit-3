# Quiz 44
## Python code
```sql
SELECT t3.account_id, t3.difference = accounts.balance AS valid
From (SELECT t1.account_id, t1.sum_amount - t2.sum_amount AS difference
FROM (
    SELECT account_id, SUM(amount) AS sum_amount
    FROM transactions
    WHERE transaction_type = "deposit"
    GROUP BY account_id
) AS t1
JOIN (
    SELECT account_id, SUM(amount) AS sum_amount
    FROM transactions
    WHERE transaction_type = "withdraw"
    GROUP BY account_id
) AS t2 ON t1.account_id = t2.account_id)
AS t3
JOIN accounts 
ON t3.account_id = accounts.customer_id;

SELECT * from customers
WHERE customer_id = 12 or customer_id = 13 or customer_id = 15 or customer_id = 17 or customer_id = 19;

```

## Output
### List with account_id and booleand value saying weather its balance is equal to the sum of deposits minus the sum of withdraws
###
![](/Assets/q44A.png)
### Names of customers marked as problematic by the previous table
###
![](/Assets/q44B.png)

## ER Diagram
![](/UML/smallcase.png)

