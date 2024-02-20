# Quiz 43
## Python code
```sql
SELECT count(*) AS table_count FROM sqlite_master WHERE type = 'table';
SELECT count(*) AS friendly_male_inhabitant_count FROM INHABITANT WHERE state = "Friendly" and gender = "Male";
SELECT avg(gold) as average_gold, V.name from INHABITANT JOIN  VILLAGE V
ON V.villageid = INHABITANT.villageid group by V.name;
SELECT COUNT(*) as items_on_A FROM ITEM WHERE item LIKE 'A%';
SELECT COUNT(DISTINCT job) as different_jobs FROM INHABITANT;
SELECT I.item as herbalist_items
FROM ITEM I
JOIN INHABITANT IH ON I.owner = IH.personid
WHERE IH.job = 'Herbalist';
```

## Output
![](/Assets/q43A.png)
![](/Assets/q43B.png)

## ER Diagram
![](/UML/cmoon.pdf)
