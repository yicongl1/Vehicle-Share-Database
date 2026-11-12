-- DROP
DROP TABLE IF EXISTS Plats, Ingredients, Contient;

-- CREATE
CREATE TABLE Plats(
    id INT,
    desi VARCHAR(60) NOT NULL,
    difficulte INT NOT NULL,
    auteur VARCHAR(60) NOT NULL,
    base INT,
    PRIMARY KEY (id),
    FOREIGN KEY (base) REFERENCES Plats(id),
    CHECK (difficulte IN (1..5)),
    UNIQUE(desi, auteur)
),

CREATE TABLE Ingredients(
    nom VARCHAR(60) NOT NULL,
    categorie VARCHAR(60) NOT NULL,
    unite VARCHAR(6) NOT NULL,
    PRIMARY KEY(nom, categorie),
    CHECK unite IN ('gramme','litre','unite')
);

CREATE TABLE Contient(
    plat INT,
    ing_nom VARCHAR(60),
    ing_cat VARCHAR(60),
    quantite float NOT NULL,
    PRIMARY KEY (plat, ing_nom, ing_cat),
    FOREIGN KEY (plat) REFERENCES Plats(id),
    FOREIGN KEY (ing_nom, ing_cat) REFERENCES Ingredients(nom, categorie),
    CHECK (quantite>0)
);

--INSERT
INSERT INTO Ingredients VALUES ('lait','entier','litre');
INSERT INTO Plats VALUES (42, 'gratin dauphinois', 3, 'blussier',NULL);
INSERT INTO Contient VALUES (42, 'lait', 'entier', 0.5);

--SELECT
/*
*/
SELECT p.auteur 
FROM Plats P, Contient C,
WHERE C.ing_nom = 'piment' AND C.ing_cat = 'rouge' 
AND C.quantite < 2.0 AND P.difficulte > 3 
AND P.desi LIKE '%gratin%';

/*
*/
SELECT I.nom, I.categorie
FROM Ingredients I LEFT OUTER JOIN Contient C ON (I.nom = C.ing_nom AND I.cat = C.ing_cat)
WHERE C.plat IS NULL

/*
*/
SELECT P.desi, P.difficulte
FROM Plats P, Contient C1, Contient C2
WHERE C1.plat = C2.plat AND C1.ing_nom = 'courgette'
AND C.plat = P.id