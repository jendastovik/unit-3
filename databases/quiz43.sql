CREATE TABLE if not EXISTS Movies2 (
    id INTEGER PRIMARY KEY,
    year INTEGER,
    budget REAL,
    dcategory VARCHAR(100),
    director VARCHAR(100),
    producer VARCHAR(100),
    name VARCHAR(100),
    genreID INTEGER NOT NULL,
    FOREIGN KEY (genreID) REFERENCES genre(id)
);



CREATE TABLE if not exists actors (
    name VARCHAR(100),
    age INTEGER,
    id INTEGER PRIMARY KEY
);

CREATE TABLE if not exists genre (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);



--INSERT INTO Movies2 (year, budget, dcategory, director, producer, name, genreID)
--VALUES (2005, 1000, 'ACTION', 'DON', 'DON', 'DON', (SELECT id FROM genre WHERE name = 'Comedy'));

select * from Movies2 join genre on genre.id = Movies2.genreID WHERE genre.name LIKE '%Comedy';
select count(*) from Movies2 join genre on genre.id = Movies2.genreID WHERE genre.name LIKE '%Comedy';

drop TABLE if exists Movies;

select AVG(budget) from Movies2;
select MAX(budget) from Movies2;
select MIN(budget) from Movies2;

select * from Movies2;

