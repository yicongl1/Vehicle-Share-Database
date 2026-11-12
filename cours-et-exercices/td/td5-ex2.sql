DROP TABLE Versions ;
DROP TABLE Documents ;
DROP TABLE Users ;

CREATE TABLE Users (
	login VARCHAR PRIMARY KEY,
	pwd VARCHAR,
	name VARCHAR
) ;

CREATE TABLE Documents (
	id INTEGER PRIMARY KEY,
	title VARCHAR,
	creator VARCHAR REFERENCES Users(login)
) ;

CREATE TABLE Versions (
	num INTEGER,
	doc INTEGER REFERENCES Documents(id),
	contrib VARCHAR REFERENCES Users(login),
  PRIMARY KEY (num, doc)
) ;

INSERT INTO Users (login, pwd, name) VALUES ('karl', 'marx', 'Karl Marx') ;
INSERT INTO Users (login, pwd, name) VALUES ('al', 'ecm2', 'Albert Einstein') ;
INSERT INTO Users (login, pwd, name) VALUES ('stc', 'nf17', 'Stéphane Crozat') ;
INSERT INTO Users (login, pwd, name) VALUES ('paul', 'mot', 'Paul Pagnol') ;

INSERT INTO Documents (id, title, creator) VALUES (1, 'Le Capital', 'karl') ;
INSERT INTO Documents (id, title, creator) VALUES (2, 'La théorie de la relativité restreinte et générale', 'al') ;
INSERT INTO Documents (id, title, creator) VALUES (3, 'Les bases de données', 'stc') ;

INSERT INTO Versions (num, doc, contrib) VALUES (1, 1, 'karl') ;
INSERT INTO Versions (num, doc, contrib) VALUES (2, 1, 'karl') ;
INSERT INTO Versions (num, doc, contrib) VALUES (3, 1, 'karl') ;
INSERT INTO Versions (num, doc, contrib) VALUES (1, 2, 'al') ;
INSERT INTO Versions (num, doc, contrib) VALUES (2, 2, 'stc') ;
INSERT INTO Versions (num, doc, contrib) VALUES (1, 3, 'stc') ;

/*
afficher le nom de l'auteur du document dont le titre est "Le Capital"
*/
SELECT u.name FROM Users u
JOIN Documents d ON u.login = d.creator
WHERE d.title = 'Le Capital';

/*
afficher les logins des users qui sont à la fois creator et contrib et qui commencent par "k"
*/
SELECT v.contrib AS login FROM Versions v
JOIN Documents d ON v.contrib = d.creator
WHERE v.contrib LIKE 'k%';

/*
Afficher les logins des users qui n'ont ni créé, ni contribué
*/
SELECT u.login FROM Users u
LEFT JOIN Documents d ON u.login = d.creator
LEFT JOIN Versions v ON u.login = v.contrib
WHERE d.creator IS NULL AND v.contrib IS NULL;

/*
afficher la dernière version (celle qui a le numéro le plus élevé) de chaque document,
la liste sera triée par id des documents croissants
*/
SELECT v.doc AS docid, MAX(v.num) AS verid FROM Versions v
GROUP BY v.doc
ORDER BY v.doc;

/*
afficher le nombre de contributions pour chaque utilisateur,
en face de leur nom, à condition que l'utilisateur ait contribué au moins 2 fois,
la liste sera triée par nombre de contributions décroissant.
*/
SELECT u.name, COUNT(v.contrib) AS nbContributions FROM Users u
JOIN Versions v ON u.login = v.contrib
GROUP BY u.name
HAVING COUNT(v.contrib) >= 2
ORDER BY COUNT(v.contrib) DESC;
