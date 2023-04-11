DROP DATABASE IF EXISTS paxhttp_notebooks;
CREATE DATABASE IF NOT EXISTS paxhttp_notebooks
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE paxhttp_notebooks;

CREATE TABLE User(
    Username varchar(50) NOT NULL,
    Password varchar(50) NOT NULL,
    PRIMARY KEY(Username)
);

CREATE TABLE Notes(
    Contents varchar(100) NOT NULL
);
