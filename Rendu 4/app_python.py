#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:01:25 2024

@author: your_user

Spyder Editor

This is a script file.
"""

import psycopg2

HOST = "localhost"
USER = "your_user"
PASSWORD = ""
DATABASE = "your_database"

try:
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    print("Connexion réussie")
    
    cur = conn.cursor()
    
    #chercher le login d'un utilisateur
    cur.execute("SELECT * FROM dpt2;")
                                                         
    #lecture ligne et affichage
    print("[N°] Nom (Population)")
    raw = cur.fetchone()
    while raw:
        print ("[0%i] %s (%i)" % (raw[0], raw[1], raw[2]))
        #print ("[",raw[0],"] ",raw[1]," (",raw[2],")")
        raw = cur.fetchone()
    #print("Visualisation de table réussie")
    
    #chercher les min-max population dans bdd
    cur.execute("SELECT MIN(population), MAX(population) FROM dpt2;")    
    raw = cur.fetchone()
    print ("Département le plus peuplé : %i\nDépartement le moins peuplé : %i" % (raw[1], raw[0]))
    
    #insérer new dpts dans bdd
    #sql = "INSERT INTO dpt2 VALUES ();"
    #cur.execute(sql)
    
    conn.close()
    
except Exception as error:
    print("Une exception s'est produite : ", error)
    print("Type D'Exception' : ", type(error))
    
    #écriture
    """cur = conn.cursor()
    cur.execute("")
    conn.commit()"""
    
    #lecture
    """cur.execute("")
    #cur.fetchone()
    cur.fetchall()"""
    
    #A faire sur Postgre : Création BDD et enregistrement fichier csv
    """cur.execute("DROP TABLE IF EXISTS dpt2;")
    cur.execute("CREATE TABLE dpt2(num INTEGER PRIMARY KEY, nom VARCHAR NOT NULL UNIQUE, population INTEGER  NOT NULL CHECK(population>0));")
    conn.commit()
    print("Création de table réussie")"""
    
    """cur.execute("\copy dpt2 (num, nom, population) FROM '/home/users/your_user/Documents/fichier.csv' WITH CSV HEADER DELIMITER ';';")     
    conn.commit()
    print("Chargement du fichier csv réussi")"""
    
    """"print(cur.fetchall())"""
    
