
CREATE TABLE users (
    username varchar(120),
    email varchar(150),
    password varchar(156),
    company varchar(200),
    age int
);

CREATE TABLE salary (
    username varchar(120),
    salary int
);

INSERT INTO users (username, email, password, company, age) 
values ('user1', 'u@d', 'pass', 'company1', 20);

SELECT email FROM users WHERE age > 20;
