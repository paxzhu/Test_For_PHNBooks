USE paxhttp_notebooks;
INSERT INTO User(author_id, Username, Password) VALUES(1, 'Tony', 'Tony'), (2, 'Mike', 'Mike'), (3, 'Li', 'Li');

INSERT INTO Article(article_id, Title, Content, author_id) VALUES
(1, 'Here is title', 'Here is content', 1),
(2, 'title2', 'content2', 1),
(3, 'title3', 'content3', 1),
(4, 'article_of_Mr2', 'Here is content', 2),
(5, 'Mr2', 'About Mr2', 2),
(6, 'Mr3', 'About Mr3', 3);