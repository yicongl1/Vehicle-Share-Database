--DROP
DROP VIEW IF EXISTS ContrainteOptionPossede, ContrainteVehiculeProprietaire, ContrainteContrat_locationEtat_des_lieux, ContrainteEntrepriseContrat_location, ContrainteLocataireContrat_location, ContrainteProprietaireContrat_location, ContrainteEntrepriseConducteur;

DROP TABLE IF EXISTS Possede, Peut_circuler, Est_disponible, Annonce, Contrat_assurance, Pays, Option, Periode, Commentaire, Facture, Etat_des_lieux, Contrat_location, Vehicule, Conducteur,Entreprise, Locataire, Proprietaire, Utilisateur;


--CREATE

CREATE TABLE Utilisateur (
	pseudo VARCHAR(255) PRIMARY KEY,
	mot_de_passe VARCHAR(255) NOT NULL,
	type VARCHAR(255) NOT NULL,
	CHECK (type='proprietaire' OR type='locataire' OR type='entreprise')
);

CREATE TABLE Proprietaire (
	pseudo VARCHAR(255) PRIMARY KEY,
	photo VARCHAR(255) NOT NULL,
	telephone VARCHAR(10) CHECK (telephone LIKE '__________') NOT NULL,
	email VARCHAR(255) NOT NULL,
	nom VARCHAR(255) NOT NULL,
	prenom VARCHAR(255) NOT NULL,
	age INT CHECK (age >= 18) NOT NULL,    
	FOREIGN KEY (pseudo) REFERENCES Utilisateur(pseudo)
);

CREATE TABLE Locataire (
	pseudo VARCHAR(255) PRIMARY KEY,
	photo VARCHAR(255) NOT NULL,
	telephone VARCHAR(10) CHECK (telephone LIKE '__________') NOT NULL,
	email VARCHAR(255) NOT NULL,
	permis VARCHAR(255) NOT NULL,
	validite DATE CHECK (validite > NOW()) NOT NULL,
	nom VARCHAR(255) NOT NULL,
	prenom VARCHAR(255) NOT NULL,
	age INT CHECK (age >= 18) NOT NULL,   	 
	FOREIGN KEY (pseudo) REFERENCES Utilisateur(pseudo)
);

CREATE TABLE Entreprise (
	pseudo VARCHAR(255) PRIMARY KEY,
	photo VARCHAR(255),
	telephone VARCHAR(10) CHECK (telephone LIKE '__________'),
	email VARCHAR(255),
	nom VARCHAR(255) NOT NULL,
	adresse VARCHAR(255) NOT NULL,
	ville VARCHAR(255) NOT NULL,
	code_postal INT CHECK (code_postal > 0 AND code_postal <= 99999) NOT NULL,
	FOREIGN KEY (pseudo) REFERENCES Utilisateur(pseudo)
);

CREATE TABLE Conducteur (
	id_conducteur SERIAL PRIMARY KEY,
	entreprise VARCHAR(255) NOT NULL,
	nom VARCHAR(255) NOT NULL,
	prenom VARCHAR(255) NOT NULL,
	age INT CHECK (age >= 18) NOT NULL,
	photo VARCHAR(255) NOT NULL,
	pseudo VARCHAR(255) NOT NULL,
	telephone VARCHAR(10) CHECK (telephone LIKE '__________') NOT NULL,
	email VARCHAR(255) NOT NULL,
	permis VARCHAR(255) NOT NULL,
	validite DATE NOT NULL,
	FOREIGN KEY (entreprise) REFERENCES Entreprise(pseudo),
	CHECK (validite > NOW())
);

CREATE TABLE Vehicule (
	immatriculation VARCHAR(255) PRIMARY KEY,
	categorie VARCHAR(255) NOT NULL,
	marque VARCHAR(255) NOT NULL,
	modele VARCHAR(255) NOT NULL,
	couleur VARCHAR(255) NOT NULL,
	carburant VARCHAR(255) NOT NULL,
	annee_mise_circulation INT NOT NULL CHECK (annee_mise_circulation > 1900 AND annee_mise_circulation < 2025),
	kilometrage INT CHECK (kilometrage > 0) NOT NULL,
	niveau_carburant FLOAT CHECK (niveau_carburant >= 0 AND niveau_carburant <= 1) NOT NULL,
	description TEXT NOT NULL,
	proprietaire VARCHAR(255) NOT NULL,
	FOREIGN KEY (proprietaire) REFERENCES Proprietaire(pseudo)
);

CREATE TABLE Contrat_location (
	id_contrat SERIAL
	 PRIMARY KEY,
	option_franchise VARCHAR(255) CHECK (option_franchise = 'sans réduction' OR option_franchise = 'franchise réduite' OR option_franchise = 'zéro franchise') NOT NULL,
	seuil_kilometrage INT NOT NULL,
	debut DATE NOT NULL,
	fin DATE NOT NULL,
	proprietaire VARCHAR(255) NOT NULL,
	vehicule VARCHAR(255),
	locataire VARCHAR(255),
	entreprise VARCHAR(255),
	FOREIGN KEY (proprietaire) REFERENCES Proprietaire(pseudo),
	FOREIGN KEY (vehicule) REFERENCES Vehicule(immatriculation),
	FOREIGN KEY (locataire) REFERENCES Locataire(pseudo),
	FOREIGN KEY (entreprise) REFERENCES Entreprise(pseudo),
	CHECK ((locataire IS NOT NULL AND entreprise IS NULL) OR (locataire IS NULL AND entreprise IS NOT NULL)),
	CHECK (seuil_kilometrage > 0)
);



CREATE TABLE Etat_des_lieux (
	id_edl SERIAL PRIMARY KEY,
	contrat INT NOT NULL,
	type VARCHAR(255) CHECK (type = 'debut' OR type = 'fin') NOT NULL,
	photo VARCHAR(255) NOT NULL,
	kilometrage INT NOT NULL,
	carburant FLOAT NOT NULL,
	checklist TEXT NOT NULL,
	FOREIGN KEY (contrat) REFERENCES Contrat_location(id_contrat),
	CHECK (kilometrage > 0),
	CHECK (carburant >= 0 AND carburant <= 1)
);




CREATE TABLE Facture (
	id_facture SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	kilometrage INT NOT NULL,
	carburant FLOAT NOT NULL,
	moyen_paiement VARCHAR(255) NOT NULL,
	montant FLOAT NOT NULL,
	contrat_location INT NOT NULL,
	FOREIGN KEY (contrat_location) REFERENCES Contrat_location(id_contrat),
	CHECK (kilometrage > 0),
	CHECK (carburant >= 0 AND carburant <= 1),
	CHECK (montant > 0)
);

CREATE TABLE Commentaire (
	id_commentaire SERIAL PRIMARY KEY,
	note INT CHECK (note >= 0 AND note <= 5) NOT NULL,
	signaler BOOLEAN NOT NULL,
	description VARCHAR(255) NOT NULL,
	contrat_location INT NOT NULL,
	FOREIGN KEY (contrat_location) REFERENCES Contrat_location(id_contrat)
);

CREATE TABLE Pays (
	nom VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Contrat_assurance (
	id_assurance SERIAL PRIMARY KEY,
	nom_assurance VARCHAR(255) NOT NULL,
	type VARCHAR(255) NOT NULL,
	vehicule VARCHAR(255) NOT NULL,
	FOREIGN KEY (vehicule) REFERENCES Vehicule(immatriculation)
);

CREATE TABLE Annonce (
	id_annonce SERIAL PRIMARY KEY,
	activite BOOLEAN NOT NULL,
	intitule VARCHAR(255) NOT NULL,
	nombre_signalement INT CHECK (nombre_signalement >= 0) NOT NULL,
	note FLOAT CHECK (note >= 0 AND note <= 5) NOT NULL,
	vehicule VARCHAR(255) NOT NULL,
	FOREIGN KEY (vehicule) REFERENCES Vehicule(immatriculation),
	CHECK (NOT(nombre_signalement >= 3 AND activite))
);

CREATE TABLE Option (
	id_option SERIAL PRIMARY KEY,
	intitule VARCHAR(255) NOT NULL
);

CREATE TABLE Periode (
	id_periode SERIAL PRIMARY KEY,
	debut DATE NOT NULL,
	fin DATE NOT NULL,
	CHECK (fin > debut)
);

CREATE TABLE Est_disponible (
	vehicule VARCHAR(255) NOT NULL,
	periode INT NOT NULL,
	PRIMARY KEY (vehicule, periode),
	FOREIGN KEY (vehicule) REFERENCES Vehicule(immatriculation),
	FOREIGN KEY (periode) REFERENCES Periode(id_periode)
);

CREATE TABLE Peut_circuler (
	vehicule VARCHAR(255) NOT NULL,
	pays VARCHAR(255) NOT NULL,
	PRIMARY KEY (vehicule, pays),
	FOREIGN KEY (vehicule) REFERENCES Vehicule(immatriculation),
	FOREIGN KEY (pays) REFERENCES Pays(nom)
);

CREATE TABLE Possede (
	vehicule VARCHAR(255) NOT NULL,
	option INT NOT NULL,
	PRIMARY KEY (vehicule, option),
	FOREIGN KEY (vehicule) REFERENCES Vehicule(immatriculation),
	FOREIGN KEY (option) REFERENCES Option(id_option)
);
