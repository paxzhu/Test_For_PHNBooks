DROP DATABASE IF EXISTS paxhttp_notebooks;
CREATE DATABASE IF NOT EXISTS paxhttp_notebooks
    DEFAULT CHARACTER SET utf8mb4 
    DEFAULT COLLATE utf8mb4_unicode_ci;
USE paxhttp_notebooks;

CREATE TABLE User(
    author_id INT NOT NULL AUTO_INCREMENT,
    Username varchar(50) NOT NULL,
    Password varchar(50) NOT NULL,
    PRIMARY KEY(author_id)
);

CREATE TABLE Article(
    article_id INT NOT NULL AUTO_INCREMENT,
    Title VARCHAR(100),
    Content TEXT,
    author_id INT,
    PRIMARY KEY(article_id),
    FOREIGN KEY(author_id) REFERENCES User(author_id)
);

