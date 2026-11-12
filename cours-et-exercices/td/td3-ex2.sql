CREATE TABLE Ligne(
  num INTEGER PRIMARY KEY CHECK(num > 0 AND num < 100),
  km INTEGER NOT NULL CHECK(km > 0 AND km < 10000)
);

CREATE TABLE Station(
  num INTEGER PRIMARY KEY,
  nom VARCHAR NOT NULL,
  adresse VARCHAR NOT NULL
);

CREATE TABLE Arrêt(
  ligne INTEGER,
  station INTEGER,
  rang INTEGER NOT NULL,
  PRIMARY KEY (ligne, station),
  FOREIGN KEY (ligne) REFERENCES Ligne(num),
  FOREIGN KEY (station) REFERENCES Station(num)
);

CREATE TABLE Conducteur(
  matricule CHAR(10) PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prénom VARCHAR NOT NULL
)

CREATE TABLE Bus(
  immat CHAR(10) PRIMARY KEY,
  type VARCHAR CHECK(type='Soufflets' OR type='Normaux' OR type='Réduits') NOT NULL,
  kilométrage INESTRICTION(Bus, immat = '5657 MA 49')JOINDRE(R1, Conducteur, R1.matricule = Conducteur.matricule)TEGER NOT NULL CHECK(kilométrage > 0 AND kilométrage < 10000000),
  matricule CHAR(10) NOT NULL REFERENCES Conducteur(matricule)
);

CREATE TABLE Trajet(
  ligne INTEGER,
  immat CHAR(10),
  nbtrajets INTEGER NOT NULL CHECK(nbtrajets > 0 AND nbtrajets < 100),
  PRIMARY KEY (ligne, immat),
  FOREIGN KEY (ligne) REFERENCES Ligne(num),
  FOREIGN KEY (immat) REFERENCES Bus(immat)
);

INSERT INTO Conducteur VALUES('AAA AAA AA', 'Baka', 'Barish');
INSERT INTO Conducteur VALUES('AAA BBB AA', 'Datou', 'Inès');
INSERT INTO Bus VALUES('5657 MA 49', 'Soufflets', 11, 'AAA AAA AA');
INSERT INTO Bus VALUES('666 XX 60', 'Normaux', 12, 'AAA BBB AA');
INSERT INTO Station VALUES(1,  'Gare SNCF', 'Paris');
INSERT INTO Ligne VALUES(42, 3);
INSERT INTO Arrêt VALUES(42, 1, 1);
INSERT INTO Trajet VALUES(42, '5657 MA 49', 3);
INSERT INTO Trajet VALUES(42, '666 XX 60', 3);

/*Q1
R1 = RESTRICTION(Bus, immat = '5657 MA 49')
R2 = JOINDRE(R1, Conducteur, R1.matricule = Conducteur.matricule)
R = PROJECTION(R2, nom, prénom)
*/
SELECT nom, prénom
FROM Bus b JOIN Conducteur c ON b.matricule = c.matricule
WHERE b.immat = '5657 MA 49';

/*Q2
Immatriculation et type des bus qui partent de la station "Gare SNCF".
R1 = RESTRICTION(Station, nom = 'Gare SNCF')
R2 = RESTRICTION(Arrêt, rang = 1)
R3 = JOINDRE(R1, R2, R1.num = R2.station)
R4 = JOINDRE(R3, Trajet, R3.ligne = Trajet.ligne)
R5 = JOINDRE(R4, Bus, R4.immat = bus.immat)
R = PROJECTION(R5, immat, type)
*/
SELECT b.immat, b.type
FROM Bus b JOIN Trajet t ON b.immat=t.immat
JOIN Arrêt a ON t.ligne = a.ligne
JOIN Station s ON s.num = a.station
WHERE s.nom = 'Gare SNCF' AND a.rang = 1

/*Q3
Numéros des lignes qui ne sont pas desservies par des bus à soufflets
波纹管巴士不提供服务的线路数量。
R1 = RESTRICTION(Bus, type = 'Soufflets')
R2 = JOINDRE(R1, Trajet, R1.immat = Trajet.immat)
R3 = JOINDREEXTERNEDROITE(R2, ligne, R2.ligne = ligne.num)
R4 = RESTRICTION(R3, Trajet.ligne IS NULL)
R = PROJECTION(R4, ligne.num)
*/
SELECT l.num
FROM (Bus b JOIN Trajet t ON b.immat=t.immat AND b.type = 'Soufflets')
RIGHTJOIN ligne l ON t.ligne = l.num
WHERE t.ligne IS NULL;