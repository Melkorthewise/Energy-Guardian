CREATE DATABASE test;

CREATE TABLE user(
    email = varchar(255),
    inlogCode = varchar(255)
);


INSERT INTO user(
    ('test@gmail.com', 'test123'),
    ('Hendrik@Yahoo.com', 'Hendrik1980'),
    ('Pino@Icloud.com', "Sesamstraat2001")
)