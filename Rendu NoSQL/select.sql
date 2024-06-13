--selectionne les vehicules avec des assurances tout risque 
SELECT
    immatriculation,
    marque,
    modele,
    annee_mise_circulation,
    Contrat_assurance->>'nom_assurance' AS nom_assurance,
    Contrat_assurance->>'type' AS type
FROM Vehicule
WHERE Contrat_assurance->>'type' = 'Tous risques';


--sélectionne des informations sur le contrat de location
SELECT
option_franchise,
seuil_kilometrage, 
debut, 
fin, 
proprietaire, 
vehicule, 
locataire, 
entreprise, 
facture ->>'montant' AS montant,
commentaire ->>'note' AS note
FROM Contrat_location;

--Selectionne tous les commentaires dont la note est de 5 
SELECT * FROM Contrat_location WHERE commentaire->>'note' = '5';

--selectionne toutes les annonces signalées
SELECT * FROM Contrat_location WHERE commentaire->>'signaler' = 'true';

--sélectionne les locataires de plus de 30 ans qui n’ont pas signalé de voitures
SELECT cl.id_contrat, cl.debut, cl.fin, l.nom, l.prenom, cl.commentaire->>'description' AS commentaire
FROM Contrat_location cl
JOIN Locataire l ON cl.locataire = l.pseudo
WHERE l.age > 30 AND cl.commentaire->>'signaler' = 'false';

--Récupere le type de contrat où l’id du contrat est 3
SELECT id_contrat, vehicule, commentaire ->> 'note' AS note_commentaire
FROM Contrat_location
WHERE id_contrat = 3;

--Récupere le montant de la facture associée au contrat de location numéro 2
SELECT id_contrat, vehicule, facture ->> 'montant' AS montant_facture
FROM Contrat_location
WHERE id_contrat = 2;
