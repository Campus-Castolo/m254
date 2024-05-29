USE testdatabase

CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL
);
