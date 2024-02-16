# Quiz 43
## Python code
```sql
SELECT count(*) FROM sqlite_master WHERE type = 'table';
SELECT count(*) FROM INHABITANT WHERE state = "Friendly" and gender = "Male";
SELECT avg(gold),count(*), V.name from INHABITANT JOIN  VILLAGE V
ON V.villageid = INHABITANT.villageid group by V.name;
SELECT COUNT(*) FROM ITEM WHERE item LIKE 'A%';
SELECT COUNT(DISTINCT job) FROM INHABITANT;
SELECT I.item
FROM ITEM I
JOIN INHABITANT IH ON I.owner = IH.personid
WHERE IH.job = 'Herbalist';
```

## Output
![](/assets/qx.png)