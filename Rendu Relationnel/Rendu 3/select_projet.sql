--Modification annonce : 
UPDATE Annonce
SET activite = FALSE, nombre_signalement = 3
WHERE id_annonce = 1;

--Suppression d’une annonce : 
DELETE FROM Annonce
WHERE id_annonce = 1;

--Consulter les annonces
SELECT A.intitule, A.note, V.categorie, V.marque, V.modele, V.annee_mise_circulation, V.carburant, V.description
FROM Vehicule V
JOIN Annonce A ON V.immatriculation = A.vehicule
JOIN Est_disponible E ON V.immatriculation = E.vehicule
JOIN Periode P ON E.periode = P.id_periode
WHERE (A.activite = TRUE) AND (P.debut > NOW());

--Moyenne d’âge : 
SELECT ROUND(AVG(annee_mise_circulation)) AS moyenne_age
FROM Vehicule;

--Kilométrage moyen
SELECT AVG(kilometrage) AS  moyenne_kilometrage
FROM Vehicule;

--Catégories les plus utilisées : 
SELECT categorie, COUNT(*) AS nombre_annonces
FROM Vehicule V
JOIN Annonce A ON V.immatriculation = A.vehicule
GROUP BY categorie
ORDER BY nombre_annonces DESC;

-- Consulter Reservation
SELECT v.modele, cl.debut, cl.fin, p.pseudo, L.pseudo, e.nom
FROM Vehicule v
JOIN Proprietaire p ON v.proprietaire = p.pseudo
JOIN Contrat_location cl ON p.pseudo = cl.proprietaire
JOIN Locataire L ON cl.locataire = l.pseudo
JOIN Entreprise e ON cl.entreprise = e.id_entreprise

-- Reservation selon plusieurs clitères
-- Ici, note supérieure à 4 et véhicule dispo le 6 mai
SELECT A.id_annonce
FROM Annonce A
JOIN Vehicule V ON V.immatriculation = A.vehicule
WHERE A.activite = TRUE 
AND A.nombre_signalement < 3     
AND A.note >= 4.0     
AND V.immatriculation NOT IN (
        SELECT vehicule
        FROM Contrat_location
        WHERE debut >= '2024-05-06' AND fin <= '2024-05-06'
    );

