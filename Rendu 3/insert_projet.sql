--telephone ? 	ENTREPRISE

--option_franchise bien check ? CONTRAT_LOCATION

--locataire AND entreprise ? CONTRAT_LOCATION

-- ANNONCE  CHECK (nombre_signalement >= 3  AND NOT activite)

INSERT INTO Utilisateur (pseudo, mot_de_passe, type)
VALUES 
    ('Gagnos', 'Gagnos', 'proprietaire'),
    ('Leplusfort', 'Leplusfort', 'proprietaire'),
    ('Xavier33', 'Xavier33', 'proprietaire'),
    ('RobertDevos', 'RobertDevos', 'proprietaire'),
    ('Chargeur2000', 'Chargeur2000', 'proprietaire'),
    ('Avellll', 'Avellll', 'proprietaire'),
    ('robot1234', 'robot1234', 'proprietaire'),
    ('millemille', 'millemille', 'proprietaire'),
    ('octogone8', 'octogone8', 'proprietaire'),
    ('davvveee', 'davvveee', 'proprietaire'),
    ('berttt', 'berttt', 'locataire'),
    ('gregou', 'gregou', 'locataire'),
    ('davidismoi', 'davidismoi', 'locataire'),
    ('marchariere', 'marchariere', 'locataire'),
    ('clavierks', 'clavierks', 'locataire'),
    ('ordi3000', 'ordi3000', 'locataire'),
    ('Raphaz', 'Raphaz', 'locataire'),
    ('mickey', 'mickey', 'locataire'),
    ('touche45', 'touche45', 'locataire'),
    ('fania', 'fania', 'locataire'),
    ('Apple', 'Apple', 'entreprise'),
    ('Amazon', 'Amazon', 'entreprise'),
    ('Google', 'Google', 'entreprise'),
    ('Meta Platforms', 'Meta Platforms', 'entreprise'),
    ('Tesla', 'Tesla', 'entreprise');

INSERT INTO Proprietaire (pseudo, photo, telephone, email, nom, prenom, age)
VALUES 
    ('Gagnos', 'gagnos.jpg', '0612345678', 'gagnos@free.fr', 'Gagnos', 'Jean', 40),
    ('Leplusfort', 'leplusfort.jpg', '0678456123', 'leplusfort@gmail.com', 'Leplusfort', 'Pierre', 35),
    ('Xavier33', 'xavier33.jpg', '0622334455', 'xavier33@yahoo.com', 'Xavier', 'Alexandre', 28),
    ('RobertDevos', 'robertdevos.jpg', '0602030405', 'robert.devos@orange.fr', 'Devos', 'Robert', 45),
    ('Chargeur2000', 'chargeur2000.jpg', '0677665544', 'chargeur2000@gmail.com', 'Chargeur', 'Lucas', 32),
    ('Avellll', 'avellll.jpg', '0654789321', 'avellll@free.fr', 'Avellll', 'Sophie', 38),
    ('robot1234', 'robot1234.jpg', '0633669988', 'robot1234@yahoo.com', 'Robot', 'Thomas', 34),
    ('millemille', 'millemille.jpg', '0611223344', 'millemille@gmail.com', 'Mille', 'Marie', 42),
    ('octogone8', 'octogone8.jpg', '0699887766', 'octogone8@orange.fr', 'Octogone', 'Nicolas', 29),
    ('davvveee', 'davvveee.jpg', '0644556677', 'davvveee@yahoo.com', 'Davvveee', 'Julie', 37);


INSERT INTO Locataire (pseudo, photo, telephone, email, permis, validite, nom, prenom, age)
VALUES 
    ('berttt', 'berttt.jpg', '0611112222', 'berttt@gmail.com', '1234567890', '2025-06-30', 'Bertrand', 'Léa', 25),
    ('gregou', 'gregou.jpg', '0622223333', 'gregou@orange.fr', '0987654321', '2024-12-31', 'Gregoire', 'Paul', 31),
    ('davidismoi', 'davidismoi.jpg', '0633334444', 'davidismoi@yahoo.com', '9876543210', '2026-03-15', 'David', 'Emma', 28),
    ('marchariere', 'marchariere.jpg', '0644445555', 'marchariere@gmail.com', '0123456789', '2025-09-22', 'Marchand', 'Louis', 35),
    ('clavierks', 'clavierks.jpg', '0655556666', 'clavierks@free.fr', '6543210987', '2024-11-18', 'Clavier', 'Anna', 27),
    ('ordi3000', 'ordi3000.jpg', '0666667777', 'ordi3000@orange.fr', '5432109876', '2025-05-10', 'Ordi', 'Thomas', 28),
    ('Raphaz', 'raphaz.jpg', '0677778888', 'raphaz@gmail.com', '2345678901', '2024-08-03', 'Raphael', 'Sophie', 31),
    ('mickey', 'mickey.jpg', '0688889999', 'mickey@yahoo.com', '7654321098', '2025-10-19', 'Mouse', 'Lucas', 27),
    ('touche45', 'touche45.jpg', '0699990000', 'touche45@free.fr', '3456789012', '2026-01-28', 'Toucher', 'Mathilde', 33),
    ('fania', 'fania.jpg', '0610101010', 'fania@gmail.com', '4567890123', '2025-07-14', 'Fania', 'Alexandra', 29);


INSERT INTO Entreprise (pseudo, photo, telephone, email, nom, adresse, ville, code_postal)
VALUES 
    ('Apple', 'apple.jpg', '0112345678', 'contact@apple.com', 'Apple Inc.', '1 Infinite Loop', 'Cupertino', 95014),
    ('Amazon', 'amazon.jpg', '0223456789', 'contact@amazon.com', 'Amazon.com, Inc.', '410 Terry Avenue North', 'Seattle', 98109),
    ('Google', 'google.jpg', '0334567890', 'contact@google.com', 'Google LLC', '1600 Amphitheatre Parkway', 'Mountain View', 94043),
    ('Meta Platforms', 'facebook.jpg', '0445678901', 'contact@facebook.com', 'Meta Platforms, Inc.', '1 Hacker Way', 'Menlo Park', 94025),
    ('Tesla', 'tesla.jpg', '0556789012', 'contact@tesla.com', 'Tesla, Inc.', '3500 Deer Creek Road', 'Palo Alto', 94304);


INSERT INTO Conducteur (id_conducteur, entreprise, nom, prenom, age, photo, pseudo, telephone, email, permis, validite)
VALUES 
    (1, 'Apple', 'Martin', 'Alexandre', 34, 'conducteur1.jpg', 'AlexTheDriver', '0611223344', 'alex.martin@amazon.com', '1234567890', '2025-05-30'),
    (2, 'Amazon', 'Dubois', 'Marie', 27, 'conducteur2.jpg', 'MarieOnTheRoad', '0622334455', 'marie.dubois@gmail.com', '0987654321', '2024-11-15'),
    (3, 'Google', 'Durand', 'Luc', 40, 'conducteur3.jpg', 'LucDriveMaster', '0633445566', 'luc.durand@yahoo.com', '9876543210', '2025-08-22'),
    (4, 'Meta Platforms', 'Leroy', 'Sophie', 31, 'conducteur4.jpg', 'SophieRider', '0644556677', 'sophie.leroy@facebook.com', '0123456789', '2026-03-10'),
    (5, 'Tesla', 'Moreau', 'Thomas', 29, 'conducteur5.jpg', 'ThomasExplorer', '0655667788', 'thomas.moreau@tesla.com', '5432109876', '2025-09-17'),
    (6, 'Apple', 'Lefevre', 'Alice', 36, 'conducteur6.jpg', 'AliTraveler', '0666777888', 'alice.lefevre@apple.com', '2345678901', '2025-07-22'),
    (7, 'Amazon', 'Garcia', 'Pierre', 33, 'conducteur7.jpg', 'PierreVoyage', '0677888999', 'pierre.garcia@google.com', '3456789012', '2026-01-12'),
    (8, 'Google', 'Fournier', 'Camille', 28, 'conducteur8.jpg', 'CamilleAdventures', '0688999000', 'camille.fournier@amazon.com', '4567890123', '2025-10-29'),
    (9, 'Meta Platforms', 'Rousseau', 'Nicolas', 35, 'conducteur9.jpg', 'NicoRoadTrip', '0699000111', 'nicolas.rousseau@tesla.com', '5678901234', '2025-04-18'),
    (10, 'Tesla', 'Petit', 'Émilie', 30, 'conducteur10.jpg', 'EmilieExplorer', '0611223344', 'emilie.petit@facebook.com', '6789012345', '2024-12-05');


INSERT INTO Contrat_location (id_contrat, option_franchise, seuil_kilometrage, debut, fin, proprietaire, locataire, entreprise)
VALUES 
    (1, 'sans réduction', 1000, '2024-05-01', '2024-05-15', 'Gagnos', 'berttt', NULL),
    (2, 'franchise réduite', 1500, '2024-06-10', '2024-06-25', 'Leplusfort', 'gregou', NULL),
    (3, 'zéro franchise', 1200, '2024-07-15', '2024-08-01', 'Xavier33', 'davidismoi', NULL),
    (4, 'sans réduction', 2000, '2024-08-20', '2024-09-05', 'RobertDevos', 'marchariere', NULL),
    (5, 'franchise réduite', 1800, '2024-09-25', '2024-10-10', 'Chargeur2000', 'clavierks', NULL),
    (6, 'zéro franchise', 1300, '2024-11-01', '2024-11-15', 'Avellll', 'ordi3000', NULL),
    (7, 'sans réduction', 1600, '2024-12-20', '2025-01-05', 'robot1234', 'Raphaz', NULL),
    (8, 'franchise réduite', 1400, '2025-01-10', '2025-01-25', 'millemille', 'mickey', NULL),
    (9, 'zéro franchise', 1700, '2025-02-05', '2025-02-20', 'octogone8', 'touche45', NULL),
    (10, 'sans réduction', 1900, '2025-03-01', '2025-03-15', 'davvveee', 'fania', NULL);

INSERT INTO Etat_des_lieux (id_edl, contrat, type, photo, kilometrage, carburant, checklist)
VALUES 
    (1, 1, 'debut', 'etatlieu1debut.jpg', 800, 0.8, 'Intérieur propre, légères rayures sur la carrosserie'),
    (2, 2, 'debut', 'etatlieu2debut.jpg', 1200, 1, 'Quelques éraflures sur le pare-chocs avant, réservoir plein'),
    (3, 3, 'debut', 'etatlieu3debut.jpg', 900, 0.7, 'Propre intérieur, légère trace sur le côté gauche'),
    (4, 4, 'debut', 'etatlieu4debut.jpg', 1500, 0.5, 'Rayures mineures sur le capot, carburant à moitié plein'),
    (5, 5, 'debut', 'etatlieu5debut.jpg', 1400, 0.4, 'Intérieur propre, impact mineur sur le côté droit'),
    (6, 6, 'debut', 'etatlieu6debut.jpg', 1100, 0.8, 'Propreté générale, léger impact sur le côté droit'),
    (7, 7, 'debut', 'etatlieu7debut.jpg', 1500, 0.4, 'Rayure sur le côté gauche, intérieur propre'),
    (8, 8, 'debut', 'etatlieu8debut.jpg', 1300, 1, 'Quelques traces sur le volant, réservoir plein'),
    (9, 9, 'debut', 'etatlieu9debut.jpg', 1400, 0.9, 'Propre et bien entretenu'),
    (10, 10, 'debut', 'etatlieu10debut.jpg', 1800, 0.3, 'Quelques petits impacts sur le pare-chocs avant, intérieur en bon état'),
    (11,1,'fin','etatlieu1fin.jpg', 900, 0.8,'Rien à signaler'),
    (12, 3, 'fin', 'etatlieu3fin.jpg', 1250, 0.5, 'Intérieur sale'),
    (13, 4, 'fin', 'etatlieu4fin.jpg', 1400, 0.5, 'Rayures mineures sur le capot, carburant à moitié plein'),
    (14, 5, 'fin', 'etatlieu5fin.jpg', 1600, 0.8, 'Légères rayures sur le rétroviseur droit'),
    (15, 6, 'fin', 'etatlieu6fin.jpg', 1250, 0.8, 'Impact sévère sur le côté droit, pare-brise brisé'),
    (16, 7, 'fin', 'etatlieu7fin.jpg', 1600, 0.5, 'Rayures sur le côté gauche, Intérieur sale'),
    (17, 8, 'fin', 'etatlieu8fin.jpg', 1250, 0.5, 'Intérieur sale'),
    (18, 9, 'fin', 'etatlieu9fin.jpg', 1500, 0.9, 'Propre et bien entretenu');

INSERT INTO Facture (id_facture, date, kilometrage, carburant, moyen_paiement, montant, contrat_location)
VALUES 
    (1, '2024-05-16', 700, 0.6, 'carte de crédit', 350.50, 1),
    (2, '2024-06-26', 900, 0.5, 'espèces', 420.75, 2),
    (3, '2024-08-02', 400, 0.8, 'chèque', 280.00, 3),
    (4, '2024-09-06', 1100, 0.7, 'virement bancaire', 520.25, 4),
    (5, '2024-10-11', 1300, 0.4, 'carte de crédit', 630.90, 5),
    (6, '2024-11-16', 1000, 0.7, 'espèces', 480.75, 6),
    (7, '2025-01-06', 1400, 0.3, 'chèque', 380.00, 7),
    (8, '2025-01-26', 1200, 0.6, 'virement bancaire', 550.25, 8),
    (9, '2025-02-21', 1500, 0.9, 'carte de crédit', 680.90, 9),
    (10, '2025-03-16', 1900, 0.2, 'espèces', 720.75, 10);


INSERT INTO Commentaire (id_commentaire, note, signaler, description, contrat_location)
VALUES 
    (1, 4, FALSE, 'Très bon véhicule, confortable et économique en carburant', 1),
    (2, 5, FALSE, 'Service impeccable, véhicule en excellent état', 2),
    (3, 3, FALSE, 'Véhicule moyen, problème de démarrage à froid', 3),
    (4, 4, FALSE, 'Conducteur très professionnel, bonnes explications', 4),
    (5, 2, TRUE, 'Véhicule sale à la remise des clés, odeur désagréable', 5),
    (6, 5, FALSE, 'Super expérience, je recommande vivement', 6),
    (7, 4, FALSE, 'Contrat clair, aucun problème lors de la restitution du véhicule', 7),
    (8, 3, FALSE, 'Petit souci technique avec le véhicule, mais rapidement résolu', 8),
    (9, 5, FALSE, 'Service clientèle très réactif, merci pour tout', 9),
    (10, 1, TRUE, 'Véhicule non conforme à la description, pneu crevé au bout de 100 km', 10);


INSERT INTO Vehicule (immatriculation, categorie, marque, modele, couleur, carburant, annee_mise_circulation, kilometrage, niveau_carburant, description, proprietaire)
VALUES 
    ('AB-123-CD', 'SUV', 'Toyota', 'Rav4', 'Noir', 'Essence', 2019, 25000, 0.7, 'Véhicule familial spacieux et confortable', 'Gagnos'),
    ('EF-456-GH', 'Compacte', 'Renault', 'Clio', 'Bleu', 'Diesel', 2020, 18000, 0.8, 'Voiture urbaine idéale pour les déplacements en ville', 'Leplusfort'),
    ('IJ-789-KL', 'Berline', 'Peugeot', '308', 'Gris', 'Essence', 2018, 30000, 0.6, 'Conduite agréable et faible consommation de carburant', 'Xavier33'),
    ('MN-012-OP', 'Berline', 'Volkswagen', 'Golf', 'Blanc', 'Essence', 2017, 35000, 0.5, 'Véhicule polyvalent, adapté à tous types de trajets', 'RobertDevos'),
    ('QR-345-ST', 'SUV', 'Ford', 'Escape', 'Rouge', 'Essence', 2021, 15000, 0.9, 'SUV compact, idéal pour les aventures en famille', 'Chargeur2000'),
    ('MN-456-ZW', 'Monospace', 'Renault', 'Espace', 'Bleu', 'Diesel', 2019, 20000, 0.6, 'Monospace spacieux et polyvalent pour les familles nombreuses', 'Avellll'),
    ('MN-789-YZ', 'Monospace', 'Citroën', 'Grand C4 Spacetourer', 'Argent', 'Essence', 2019, 22000, 0.7, 'Monospace familial spacieux et polyvalent avec une conduite agréable', 'robot1234'),
    ('BR-789-QR', 'Break', 'Volkswagen', 'Passat Variant', 'Blanc', 'Diesel', 2021, 12000, 0.9, 'Break élégant et confortable avec un grand espace de chargement', 'millemille'),
    ('BR-456-WX', 'Break', 'Peugeot', '508 SW', 'Gris', 'Diesel', 2020, 18000, 0.8, 'Break élégant et confortable avec un design moderne', 'octogone8'),
    ('UT-234-ST', 'Utilitaire', 'Ford', 'Transit', 'Blanc', 'Diesel', 2020, 25000, 0.5, 'Utilitaire fiable et robuste, idéal pour les professionnels', 'davvveee');


INSERT INTO Pays (nom)
VALUES 
    ('France'),
    ('Espagne'),
    ('Italie'),
    ('Allemagne'),
    ('Royaume-Uni');


INSERT INTO Contrat_assurance (id_assurance, nom_assurance, type, vehicule)
VALUES 
    (1, 'Assurance Auto Plus', 'Tous Risques', 'AB-123-CD'),
    (2, 'Assurance Zéro Tracas', 'Responsabilité Civile', 'EF-456-GH'),
    (3, 'Assurance Sérénité', 'Tous Risques', 'IJ-789-KL'),
    (4, 'Assurance Tranquillité', 'Responsabilité Civile', 'MN-012-OP'),
    (5, 'Assurance Protection Totale', 'Tous Risques', 'QR-345-ST');


INSERT INTO Annonce (id_annonce, activite, intitule, nombre_signalement, note, vehicule)
VALUES 
    (1, TRUE, 'ma voiture', 0, 4.2, 'AB-123-CD'),
    (2, FALSE, 'Location pas cher', 0, 4.8, 'EF-456-GH'),
    (3, TRUE, 'Mon bebe mon bolide', 0, 4.5, 'IJ-789-KL'),
    (4, FALSE, 'en promo', 0, 4.7, 'MN-012-OP'),
    (5, TRUE, 'la plus grande voiture de lannée', 0, 4.4, 'QR-345-ST');


INSERT INTO Option (id_option, intitule)
VALUES 
    (1, 'GPS'),
    (2, 'Siège enfant'),
    (3, 'Climatisation'),
    (4, 'Assistance au stationnement'),
    (5, 'Toit panoramique'),
    (6, 'Système audio premium'),
    (7, 'Sièges chauffants'),
    (8, 'Détection des angles morts');

INSERT INTO Periode (id_periode, debut, fin)
VALUES 
    (1, '2024-05-01', '2024-05-15'),
    (2, '2024-06-01', '2024-06-15'),
    (3, '2024-07-01', '2024-07-15'),
    (4, '2024-08-01', '2024-08-15'),
    (5, '2024-09-01', '2024-09-15');

INSERT INTO Est_disponible (vehicule, periode)
VALUES 
    ('AB-123-CD', 1),
    ('EF-456-GH', 2),
    ('IJ-789-KL', 3),
    ('MN-012-OP', 4),
    ('QR-345-ST', 5);

INSERT INTO Peut_circuler (vehicule, pays)
VALUES 
    ('AB-123-CD', 'France'),
    ('AB-123-CD', 'Espagne'),
    ('EF-456-GH', 'France'),
    ('IJ-789-KL', 'Italie'),
    ('MN-012-OP', 'Allemagne'),
    ('QR-345-ST', 'Royaume-Uni');

INSERT INTO Possede (vehicule, option)
VALUES 
    ('AB-123-CD', 1),
    ('AB-123-CD', 3),
    ('EF-456-GH', 2),
    ('EF-456-GH', 3),
    ('IJ-789-KL', 1),
    ('MN-012-OP', 3),
    ('QR-345-ST', 1),
    ('QR-345-ST', 3),
    ('QR-345-ST', 5);

CREATE VIEW ContrainteEntrepriseConducteur AS
SELECT pseudo 
FROM Entreprise
WHERE pseudo NOT IN (SELECT entreprise FROM Conducteur);

CREATE VIEW ContrainteProprietaireContrat_location AS
SELECT pseudo 
FROM Proprietaire
WHERE pseudo NOT IN (SELECT proprietaire FROM Contrat_location);

CREATE VIEW ContrainteLocataireContrat_location AS
SELECT pseudo 
FROM Locataire
WHERE pseudo NOT IN (SELECT locataire FROM Contrat_location);

CREATE VIEW ContrainteEntrepriseContrat_location AS
SELECT pseudo
FROM Entreprise
WHERE pseudo NOT IN (SELECT entreprise FROM Contrat_location);

CREATE VIEW ContrainteContrat_locationEtat_des_lieux AS
SELECT id_contrat
FROM Contrat_location
WHERE id_contrat NOT IN (SELECT contrat FROM Etat_des_lieux);

CREATE VIEW ContrainteVehiculeProprietaire AS
SELECT proprietaire
FROM Vehicule
WHERE proprietaire NOT IN (SELECT pseudo FROM Proprietaire);

CREATE VIEW ContrainteOptionPossede AS
SELECT id_option
FROM Option
WHERE id_option NOT IN (SELECT option FROM Possede);


