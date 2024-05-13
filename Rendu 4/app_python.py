#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:01:25 2024

@author: your_user

Spyder Editor

This is a script file.
"""

import psycopg2

HOST = 'localhost'
USER = 'your_user'
PASSWORD = 'your_password'
DATABASE = 'your_database'

#pour la creation de user, il faut check si le pseudo est pris
def check_pseudo_availability(connection, username):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE pseudo = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            print("Le nom d'utilisateur est déjà pris.")
            return False
        else:
            print("Le nom d'utilisateur est disponible.")
            return True
    except psycopg2.Error as e:
        print("Erreur lors de la vérification de l'existence du nom d'utilisateur:", e)
        return False

#supprimer utilisateur
def delete_user(connection, pseudo):
   try:
       cursor = connection.cursor()
       pseudo = str(input("Entrez le pseudo de l’utilisateur à supprimer : "))
       query = "SELECT * FROM Utilisateur WHERE pseudo = %s;"
       cursor.execute(query, (pseudo,))
       if cursor.rowcount > 0:
           query = "DELETE FROM Utilisateur WHERE pseudo = %s;"
           cursor.execute(query, (pseudo,))
           print("L’utilisateur a été supprimé avec succès !")
       else:
           print("Aucun utilisateur n’a été trouvé avec ce pseudo.")
       connection.commit()
   except psycopg2.Error as error:
       print("Erreur lors de la suppression de l’utilisateur :", error)

#activer utilisateur
def activate_user(connection, pseudo):
   try:
       cursor = connection.cursor()
       query = "SELECT * FROM Utilisateur WHERE pseudo = %s;"
       cursor.execute(query, (pseudo,))
       if cursor.rowcount > 0:
           query = "UPDATE Utilisateur SET actif = TRUE WHERE pseudo = %s;"
           cursor.execute(query, (pseudo,))
           print("L’utilisateur a été supprimé avec succès !")
       else:
           print("Aucun utilisateur n’a été trouvé avec ce pseudo.")
       connection.commit()
   except psycopg2.Error as error:
       print("Erreur lors de l'activation de l’utilisateur :", error)

#Verification de mot de passe
def login(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE pseudo = %s AND mot_de_passe = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            print("Connexion réussie")
            return user[2]  # Renvoyer le type d'utilisateur
        else:
            print("Nom d'utilisateur ou mot de passe incorrect")
            return None
    except psycopg2.Error as e:
        print("Échec de la connexion:", e)
        return None

#inserer nouveau proprietaire
def insert_new_proprietaire_with_input(connection, pseudo):
    try:
        cursor = connection.cursor()
        photo = input("Photo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input("Age: "))
        insert_query = "INSERT INTO Proprietaire (pseudo, photo, telephone, email, nom, prenom, age) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (pseudo, photo, telephone, email, nom, prenom, age))
        connection.commit()
        activate_user(connection, pseudo)
        print("Nouveau propriétaire inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau propriétaire:", error)

#inserer nouveau locataire
def insert_new_locataire_with_input(connection, pseudo):
    try:
        cursor = connection.cursor()
        photo = input("Photo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        permis = input("Permis: ")
        validite = input("Validité: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input("Age: "))
        insert_query = "INSERT INTO Locataire (pseudo, photo, telephone, email, permis, validite, nom, prenom, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (pseudo, photo, telephone, email, permis, validite, nom, prenom, age))
        connection.commit()
        activate_user(connection, pseudo)
        print("Nouveau locataire inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau locataire:", error)

#inserer nouvelle entreprise
def insert_new_entreprise_with_input(connection, pseudo):
   try:
       cursor = connection.cursor()
       photo = input("Photo: ")
       telephone = input("Téléphone: ")
       email = input("Email: ")
       nom = input("Nom: ")
       adresse = input("Adresse: ")
       ville = input("Ville: ")
       code_postal = input("Code postal: ")
       insert_query = "INSERT INTO Entreprise (pseudo, photo, telephone, email, nom, adresse, ville, code_postal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
       cursor.execute(insert_query, (pseudo, photo, telephone, email, nom, adresse, ville, code_postal))
       connection.commit()
       activate_user(connection, pseudo)
       print("Nouvelle entreprise insérée avec succès !")
   except psycopg2.Error as error:
       print("Erreur lors de l'insertion de la nouvelle entreprise:", error)

#creation d’utilisateur
def create_user(connection):
    pseudo = input("Veuillez entrer un nom d'utilisateur : ")
    while not check_pseudo_availability(connection, pseudo):
        pseudo = input("Veuillez entrer un autre nom d'utilisateur : ")
    
    password = input("Veuillez entrer un mot de passe : ")
    confirm_password = input("Veuillez confirmer votre mot de passe : ")
    while password != confirm_password:
        print("Les mots de passe ne correspondent pas.")
        password = input("Veuillez entrer un mot de passe : ")
        confirm_password = input("Veuillez confirmer votre mot de passe : ")
    
    user_type = input("Veuillez entrer le type d'utilisateur (proprietaire/locataire/entreprise) : ")
    while user_type not in ["proprietaire", "locataire", "entreprise"]:
        print("Type d'utilisateur invalide.")
        user_type = input("Veuillez entrer le type d'utilisateur (proprietaire/locataire/entreprise) : ")
    
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Utilisateur (pseudo, mot_de_passe, type, actif) VALUES (%s, %s, %s, FALSE)", (pseudo, password, user_type))
        connection.commit()
        print("Utilisateur créé avec succès.")
        cursor.close()
        
        # Appeler la fonction correspondante en fonction du type d'utilisateur
        if user_type == "proprietaire":
            insert_new_proprietaire_with_input(connection, pseudo)
        elif user_type == "locataire":
            insert_new_locataire_with_input(connection, pseudo)
        elif user_type == "entreprise":
            insert_new_entreprise_with_input(connection, pseudo)

    except psycopg2.Error as e:
        print("Erreur lors de la création de l'utilisateur :", e)

#vérifier si le véhicule existe
def check_vehicule_existence(connection, vehicule, pseudo):
   try:
       cursor = connection.cursor()
       cursor.execute("SELECT * FROM Vehicule WHERE immatriculation = %s AND proprietaire = %s", (vehicule, pseudo,))
       user = cursor.fetchone()
       cursor.close()
       if user:
           print("La voiture est enregistrée dans la base de données")
           return True
       else:
           print("La voiture n'est pas enregistrée dans la base de données")
           return False
   except psycopg2.Error as e:
       print("Erreur lors de la vérification de l'enregistrement du véhicule", e)
       return False

#vérifier si un véhicule possède déjà une annonce 
def check_vehicule_availability(connection, vehicule):
   try:
       cursor = connection.cursor()
       cursor.execute("SELECT * FROM Annonce WHERE vehicule  = %s", (vehicule,))
       user = cursor.fetchone()
       cursor.close()
       if user:
           print("La voiture possède une annonce")
           return False
       else:
           print("La voiture ne possède pas d'annonces")
           return True
   except psycopg2.Error as e:
       print("Erreur lors de la vérification de l'existence du véhicule dans les annonces", e)
       return False

#inserer nouvelle annonce
def insert_new_announcement_with_input(connection, pseudo):
    try:
        cursor = connection.cursor()
        activite = input("Activité (True/False): ")
        intitule = input("Intitulé (Voiture à louer): ")
        nombre_signalement = 0
        note = float(input("Note (Entre 0 et 5): "))
        vehicule = input("Véhicule (AB-123-CD): ")
        existence = check_vehicule_existence(connection, vehicule, pseudo)
        availability = False
        if existence:
            availability  = check_vehicule_availability(connection, vehicule)        
        while ((not existence) or (not availability)):
            if existence:
                vehicule = input("Veuillez entrer un autre vehicule : ")
                availability  = check_vehicule_availability(connection, vehicule)
            else:
                vehicule = input("Veuillez entrer un vehicule déjà existant : ")
                existence = check_vehicule_existence(connection, vehicule)
        """elif not availability:
                vehicule = input("Veuillez entrer un autre vehicule : ")
                availability  = check_vehicule_availability(connection, vehicule)"""
        insert_query = "INSERT INTO Annonce (activite, intitule, nombre_signalement, note, vehicule) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (activite, intitule, nombre_signalement, note, vehicule))
        connection.commit()
        print("Nouvelle annonce insérée avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion de la nouvelle annonce:", error)

def insert_new_conducteur_with_input(connection, pseudo):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id_conducteur) FROM Conducteur;")
        max_id = cursor.fetchone()[0]
        if max_id is None:
            max_id = 0
        id_conducteur = max_id + 1
        
        entreprise  = pseudo
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input("age: "))
        photo = input("Photo: ")
        pseudo = input("Pseudo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        permis = input("Permis: ")
        validite = input("Validité: ")
        insert_query = "INSERT INTO Conducteur (id_conducteur, entreprise, nom, prenom, age, photo, pseudo, telephone, email, permis, validite) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (id_conducteur, entreprise, nom, prenom, age, photo, pseudo, telephone, email, permis, validite))
        connection.commit()
        print("Nouveau conducteur inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau conducteur:", error)


try:
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    print("Connexion à la BDD réussie")
    
    
    """choix = ''
    while (choix != 'oui' and choix != 'non') :
        print("choix invalide, veuillez recommencer")
        choix = str(input("Voulez vous faire une rehcerche par critères (oui/non)\n"))"""
        
    '''
    
    #test existence pseudo
    pseudo_test = "Gagnos"
    check_pseudo_availability(conn, pseudo_test)
    pseudo_test = "NewPseudo"
    check_pseudo_availability(conn, pseudo_test)
    
    #test pouvoir se connecter
    pseudo_test = "Gagnos"
    print("Login: ", pseudo_test)
    password_test = str(input("Password: "))
    type_test = login(conn, pseudo_test, password_test)
    if (type_test != None):
        print("Vous êtes", type_test)
    
    #test ajouter une annonce
    print("Vous allez ajouter une annonce, veuillez renseigner les informations")    
    if (type_test == "proprietaire"):
        insert_new_announcement_with_input(conn)
    else:
        print("Vous n'êtes pas proprietaire, vous ne pouvez pas ajouter d'annonce !")
        
    """#test ajouter un utilisateur
    print("Vous allez vous inscrire, veuillez renseigner les informations") 
    create_user(conn)"""
    '''
    insert_new_conducteur_with_input(conn, "Tesla")
    
    #delete_old_user(connection)
    
    conn.close()
    print("Déconnexion de la BDD réussie")
    
except Exception as error:
    print("Une exception s'est produite : ", error)
    print("Type D'Exception' : ", type(error))

    
