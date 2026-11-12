DROP TABLE IF EXISTS dpt2;

CREATE TABLE dpt2 (
    num INTEGER PRIMARY KEY,
    nom VARCHAR(100),
    pop INTEGER
);

 \copy dpt2(num, nom, pop) FROM '/chemin/vers/dpt2.csv' WITH CSV HEADER DELIMITER ';' QUOTE '"';