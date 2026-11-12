DROP TABLE IF EXISTS Dessert_Site;
DROP TABLE IF EXISTS Arret_Bus;
DROP TABLE IF EXISTS Site_Touristique;

CREATE TABLE Arret_Bus(
Ligne INTEGER,
horaire TIME,
PRIMARY KEY(ligne, horaire)
);

CREATE TABLE Site_Touristique(
nom VARCHAR PRIMARY KEY,
anciennete INTEGER
);

CREATE TABLE Dessert_Site(
bus_ligne INTEGER,
bus_horaire TIME,
site VARCHAR,
PRIMARY KEY (bus_ligne, bus_horaire, site),
FOREIGN KEY (bus_ligne, bus_horaire) REFERENCES Arret_Bus(ligne, horaire),
FOREIGN KEY(site) REFERENCES Site_Touristique(nom)
);

INSERT INTO Arret_de_bus VALUES(1, TIME '11:00:00');
INSERT INTO Arret_de_bus VALUES(1, TIME '11:10:00');
INSERT INTO Arret_de_bus VALUES(1, TIME '21:12:00');
INSERT INTO Arret_de_bus VALUES(2, TIME '12:35:00');
                      ^
INSERT INTO SiteTouristique  VALUES('Chateau', 128);
INSERT INTO SiteTouristique  VALUES('Porte', 2150);
INSERT INTO Dessert_Site VALUES(1, TIME '11:00:00', 'Chateau');
INSERT INTO Dessert_Site VALUES(1, TIME '11:10:00', 'Porte');
INSERT INTO Dessert_Site VALUES(2, TIME '12:35:00', 'Chateau');
INSERT INTO Dessert_Site VALUES(2, TIME '12:35:00', 'Porte');
