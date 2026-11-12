# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:46:00 2024
"""

import psycopg2
 
HOST = 'localhost'
USER = 'your_user'
PASSWORD = 'your_password'
DATABASE = 'your_database'
 
try:
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST,DATABASE,USER,PASSWORD))
    print('Connexion réussie')
    cur = conn.cursor()

    sql = "SELECT num,nom,pop FROM dpt2;"
    cur.execute(sql)
    conn.commit()
    raw = cur.fetchone()
    dptmin = raw[2]
    dptmax = raw[2]
    print ("[N°] NOM (Population)")
    while raw:
        print ("[0%i] %s (%s)" % (raw[0], raw[1], raw[2]))
        if raw[2] > dptmax: dptmax = raw[2] 
        if raw[2] < dptmin: dptmin = raw[2] 
        raw = cur.fetchone()

    print ("> Département le plus peuplé :  %i" % dptmax)
    print ("> Département le moin peuplé :  %i" % dptmin)

    req_add = "INSERT INTO dpt2 VALUES('11','Val-dOise','1256607');"
    cur.execute(req_add)


    input_num1 = int(input("Entrez le num du dpt:"))
    req_del = "DELETE FROM dpt2 WHERE num = %d;" % (input_num1)
    cur.execute(req_del)

    input_num2=int(input("Entrez le num du dpt:"))
    input_population=int(input("Entrez le population du dpt:"))
    req_update="UPDATE dpt2 SET pop=%d WHERE num=%d;" % (input_num2,input_population)
    cur.execute(req_update)
    conn.commit()

    conn.close()
except Exception as error:
        print("Une exception s'est produite : ",error)
        print("Type D'Exception : ",type(error))
        
        
        
#inserer nouvelle annonce
def insert_new_announcement_with_input(connection):
    try:
        cursor = connection.cursor()
        activite = input("Activité (True/False): ")
        intitule = input("Intitulé: ")
        nombre_signalement = int(input("Nombre de signalements: "))
        note = float(input("Note: "))
        vehicule = input("Véhicule: ")
        insert_query = "INSERT INTO Annonce (activite, intitule, nombre_signalement, note, vehicule) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (activite, intitule, nombre_signalement, note, vehicule))
        connection.commit()
        print("Nouvelle annonce insérée avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion de la nouvelle annonce:", error)

#inserer nouvelle entreprise
def insert_new_entreprise_with_input(connection):
    try:
        cursor = connection.cursor()
        photo = input("Photo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        nom = input("Nom: ")
        adresse = input("Adresse: ")
        ville = input("Ville: ")
        code_postal = input("Code postal: ")
        insert_query = "INSERT INTO Entreprise (photo, telephone, email, nom, adresse, ville, code_postal) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (photo, telephone, email, nom, adresse, ville, code_postal))
        connection.commit()
        print("Nouvelle entreprise insérée avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion de la nouvelle entreprise:", error)

#inserer nouvel locataire
def insert_new_locataire_with_input(connection):
    try:
        cursor = connection.cursor()
        pseudo = input("Pseudo: ")
        photo = input("Photo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        permis = input("Permis: ")
        validite = input("Validité: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input(" ge: "))
        insert_query = "INSERT INTO Locataire (pseudo, photo, telephone, email, permis, validite, nom, prenom, age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (pseudo, photo, telephone, email, permis, validite, nom, prenom, age))
        connection.commit()
        print("Nouveau locataire inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau locataire:", error)

#inserer nouveau proprietaire
def insert_new_proprietaire_with_input(connection):
    try:
        cursor = connection.cursor()
        pseudo = input("Pseudo: ")
        photo = input("Photo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input(" ge: "))
        insert_query = "INSERT INTO Proprietaire (pseudo, photo, telephone, email, nom, prenom, age) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (pseudo, photo, telephone, email, nom, prenom, age))
        connection.commit()
        print("Nouveau propriétaire inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau propriétaire:", error)

#inserer nouveau conducteur
def insert_new_conducteur_with_input(connection):
    try:
        cursor = connection.cursor()
        id_conducteur = int(input("ID Conducteur: "))
        entreprise = int(input("Entreprise: "))
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input(" ge: "))
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
