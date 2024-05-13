import datetime
import psycopg2
HOST = "localhost"
USER = "your_user"
PASSWORD = "your_password"
DATABASE = "your_database"


# pour la creation de user, il faut check si le pseudo est pris
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


# supprimer utilisateur
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


# activer utilisateur
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


# Verification de mot de passe
def login(connection, username, password):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE pseudo = %s AND mot_de_passe = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            print("Connexion réussie")
            return True,user[2]  # Renvoyer le type d'utilisateur
        else:
            print("Nom d'utilisateur ou mot de passe incorrect")
            return None
    except psycopg2.Error as e:
        print("Échec de la connexion:", e)
        return None


# inserer nouveau proprietaire
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


# inserer nouveau locataire
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


# inserer nouvelle entreprise
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


# creation d’utilisateur
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
        cursor.execute("INSERT INTO Utilisateur (pseudo, mot_de_passe, type, actif) VALUES (%s, %s, %s, FALSE)",
                       (pseudo, password, user_type))
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


# vérifier si le véhicule existe
def check_vehicule_existence(connection, vehicule):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Vehicule WHERE immatriculation = %s", (vehicule,))
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


# vérifier si un véhicule possède déjà une annonce
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


# inserer nouvelle annonce
'''def insert_new_announcement_with_input(connection):
    try:
        cursor = connection.cursor()
        activite = input("Activité (True/False): ")
        intitule = input("Intitulé (Voiture à louer): ")
        nombre_signalement = 0
        note = float(input("Note (Entre 0 et 5): "))
        vehicule = input("Véhicule (AB-123-CD): ")
        while not check_vehicule_existence(connection, vehicule):
            vehicule = input("Veuillez entrer un vehicule déjà existant : ")
        while not check_vehicule_availability(connection, vehicule):
            vehicule = input("Veuillez entrer un autre vehicule : ")
        insert_query = "INSERT INTO Annonce (activite, intitule, nombre_signalement, note, vehicule) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (activite, intitule, nombre_signalement, note, vehicule))
        connection.commit()
        print("Nouvelle annonce insérée avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion de la nouvelle annonce:", error)'''

def insert_new_conducteur_with_input(connection, pseudo):
    try:
        cursor = connection.cursor()
        entreprise  = pseudo
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        age = int(input("Age: "))
        photo = input("Photo: ")
        pseudo = input("Pseudo: ")
        telephone = input("Téléphone: ")
        email = input("Email: ")
        permis = input("Permis: ")
        validite = input("Validité: ")
        insert_query = "INSERT INTO Conducteur (entreprise, nom, prenom, age, photo, pseudo, telephone, email, permis, validite) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (entreprise, nom, prenom, age, photo, pseudo, telephone, email, permis, validite,))
        connection.commit()
        print("Nouveau conducteur inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau conducteur:", error)

def Consulter_Annonce(connection) :
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM Annonce WHERE activite = TRUE;"
        cursor.execute(query)
        row = cursor.fetchone()
        while row :
            print(f"annonce {row[0]} : {row[2]} note : {row[4]} vehicule = {row[5]}")
            row = cursor.fetchone()
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau conducteur:", error)


def insert_new_comment_with_input(connection, user_type, username):
    try:
        cursor = connection.cursor()
        contrat_location = int(input("ID du contrat de location: "))

        if user_type == "locataire":
            query = "SELECT locataire FROM Contrat_location WHERE id_contrat = %s;"
            cursor.execute(query, (contrat_location,))
            row = cursor.fetchone()
            if row[0] != username:
                print("Ce n'est pas votre contrat de location, veuillez réessayer")
                return
        elif user_type == "entreprise":
            query = "SELECT locataire FROM Contrat_location WHERE id_contrat = %s;"
            cursor.execute(query, (contrat_location,))
            row = cursor.fetchone()
            if row[0] != username:
                print("Ce n'est pas votre contrat de location, veuillez réessayer")
                return

        query = "SELECT fin FROM Contrat_location WHERE id_contrat = %s;"
        cursor.execute(query, (contrat_location,))
        row = cursor.fetchone()
        if row[0] > datetime.date.today():
            print("le contrat n'est pas fini, il est impossible d'ajouter un commentaire")
            return

        query = "SELECT * FROM Commentaire WHERE contrat_location = %s;"
        cursor.execute(query, (contrat_location,))

        row = cursor.fetchone()
        if row:
            print("Il y a déjà un commentaire pour ce contrat de location")
            return

        note = int(input("Note (entre 1 et 5): "))
        signaler = input("Signaler (True/False): ").lower() == 'true'
        description = input("Description: ")
        insert_query = "INSERT INTO Commentaire (note, signaler, description, contrat_location) VALUES (%s, %s, %s, %s);"
        cursor.execute(insert_query, (note, signaler, description, contrat_location))

        ##mise à jour de la note de l'annonce
        query = "SELECT vehicule FROM Contrat_location WHERE id_contrat = %s;"
        cursor.execute(query, (contrat_location,))
        row = cursor.fetchone()
        vehicule = row[0]

        query = "SELECT note FROM Commentaire co, Contrat_location cl WHERE cl.id_contrat = co.contrat_location AND cl.vehicule = %s;"
        cursor.execute(query, (vehicule,))
        row = cursor.fetchone()
        somme = 0
        cpt = 0
        while row:
            somme += row[0]
            cpt += 1
            row = cursor.fetchone()

        somme = somme / cpt

        query = "UPDATE Annonce SET note = %s WHERE vehicule = %s;"
        cursor.execute(query, (somme, vehicule,))
        connection.commit()
        print("Nouveau commentaire inséré avec succès !")
    except psycopg2.Error as error:
        print("Erreur lors de l'insertion du nouveau commentaire:", error)

def Rerserver_Voiture(conn, locataire: str, entreprise: str) -> int:
    idAnnonce: int = int(input("Veuillez entrer le numéro de l'annonce que vous souhaitez réserver"))
    date_debut_str: str = input("Veuillez saisir une date de début de location au format YYYY-MM-DD : ")
    date_debut_valide: bool = False

    date_debut = None

    while not date_debut_valide:
        try:
            date_debut = datetime.datetime.strptime(date_debut_str, "%Y-%m-%d").date()
            if date_debut > datetime.date.today():
                date_debut_valide = True
            else:
                print("Vous ne pouvez pas réserver une annonce dans le passé, veuillez recommencer")
                date_debut_str = input("Veuillez saisir une date de début valide au format YYYY-MM-DD")
        except ValueError:
            print("Format de date incorrect.")
            date_debut_str = input("Veuillez saisir une date de début valide au format YYYY-MM-DD")

    date_fin_str = input("Veuillez saisir une date de fin de location au format YYYY-MM-DD : ")
    date_fin_valide: bool = False

    date_fin = None

    while not date_fin_valide:
        try:
            date_fin = datetime.datetime.strptime(date_fin_str, "%Y-%m-%d").date()
            if date_fin > date_debut:
                date_fin_valide = True
            else:
                print("La fin de location ne peut pas être avant la fin de la location, veuillez recommencer")
                date_fin_str = input("Veuillez saisir une date de début valide au format YYYY-MM-DD")
        except ValueError:
            print("Format de date incorrect.")
            date_fin_str = input("Veuillez saisir une date de début valide au format YYYY-MM-DD")

    ##Verifications pour savoir si la date correspond bien à une péiode où le véhicule peut
    ##être loué ou que quelqu'un d'autre n'a pas déjà loué le véhicule sur cette période
    requete: str = f"SELECT cl.debut, cl.fin FROM Contrat_location cl, Vehicule V, Annonce A, Proprietaire P WHERE cl.proprietaire = P.pseudo AND V.proprietaire = P.pseudo AND A.vehicule = V.immatriculation AND A.id_annonce = {idAnnonce};"
    cur = conn.cursor()
    cur.execute(requete)

    row = cur.fetchone()
    vehicule_deja_occupe: bool = False
    while row:
        # Convertir la date SQL en un objet datetime
        date_debut_location_existante = row[0]
        date_fin_location_existante = row[1]

        if (date_debut_location_existante < date_debut and date_fin_location_existante > date_debut) or (
            date_debut_location_existante < date_fin and date_fin_location_existante > date_fin) or (
            date_debut < date_debut_location_existante and date_fin >date_fin_location_existante):
            vehicule_deja_occupe = True
        row = cur.fetchone()

    if vehicule_deja_occupe:
        print("le véhicule est indisponible pendant cette période, veuillez recommencer")
        return 0

    requete = f"SELECT P.debut, P.fin FROM Periode P, Vehicule V, Annonce A, Est_disponible E WHERE P.id_periode = E.periode AND E.vehicule = V.immatriculation AND V.immatriculation = A.vehicule AND A.id_annonce = {idAnnonce};"
    cur.execute(requete)

    row = cur.fetchone()
    vehicule_indisponible: bool = True
    while row:
        # Convertir la date SQL en un objet datetime
        date_debut_periode = row[0]
        date_fin_periode = row[1]
        if (date_debut_periode < date_debut and date_fin < date_fin_periode ):
            vehicule_indisponible = False
        row = cur.fetchone()

    if vehicule_indisponible:
        print("le véhicule est indisponible pendant cette période, veuillez recommencer")
        return 0

    option_franchise = str(
        input("Veuillez choisir une option de franchise : (sans réduction/franchise réduite/zéro franchise)")).lower()
    while option_franchise not in ["sans réduction", "franchise réduite", "zéro franchise"]:
        option_franchise = str(
            input("Veuillez choisir une option de franchise : (sans réduction/franchise réduite/zéro franchise)")).lower()

    seuil_kilometrage = int(input("Veuillez choisir le seuil de kilométrage souhaité durant la location"))
    while seuil_kilometrage < 0:
        option_franchise = int(input("Veuillez choisir le seuil de kilométrage souhaité durant la location"))

    requete = f"SELECT pseudo, V.immatriculation FROM Proprietaire P, Annonce A, Vehicule V WHERE P.pseudo = V.proprietaire AND V.immatriculation = A.vehicule AND A.id_annonce = {idAnnonce};"
    cur.execute(requete)
    row = cur.fetchone()
    proprietaire = row[0]
    vehicule = row[1]

    ##Insertion du contrat de location
    if entreprise == None:
        requete = f"INSERT INTO Contrat_location(option_franchise, seuil_kilometrage, debut, fin, proprietaire, vehicule, locataire) VALUES ('{option_franchise}',{seuil_kilometrage},'{date_debut}', '{date_fin}', '{proprietaire}', '{vehicule}', '{locataire}');"
    else:
        requete = f"INSERT INTO Contrat_location(option_franchise, seuil_kilometrage, debut, fin, proprietaire, vehicule, entreprise) VALUES ('{option_franchise}',{seuil_kilometrage},'{date_debut}', '{date_fin}', '{proprietaire}', '{vehicule}', '{entreprise}');"

    print("La réservation a bien été prise en compte")

    cur.execute(requete)
    conn.commit()
    return 1


def Etat_des_lieux(connection):
    cur = connection.cursor()
    id_contrat = input("Entrez l'ID du contrat de location : ")
    cur.execute("SELECT id_contrat FROM Contrat_location WHERE id_contrat = %s", (id_contrat,))
    contrat = cur.fetchone()
    if not contrat:
        print("Le contrat de location spécifié n'existe pas.")
        return

    type_edl = input("Entrez le type d'état des lieux (debut/fin) : ").lower()
    while type_edl not in ('debut', 'fin'):
        print("Le type d'état des lieux doit être 'debut' ou 'fin'.")
        type_edl = input("Entrez le type d'état des lieux (debut/fin) : ").lower()

    query = "SELECT * FROM Etat_des_lieux WHERE contrat = %s and type = %s;"
    cur.execute(query, (id_contrat, type_edl,))
    row = cur.fetchone()
    if row :
        print("Cet etat des lieux a déjà été rentré")
        return

    if type_edl == 'debut':
        query = "SELECT debut FROM Contrat_location WHERE id_contrat = %s;"
        cur.execute(query, (id_contrat,))
        date_debut = cur.fetchone()
        if datetime.date.today() < date_debut[0]:
            print("Impossible d'entrer un etat des lieux dans le futur")
            return
    elif type_edl == 'fin':
        query = "SELECT fin FROM Contrat_location WHERE id_contrat = %s;"
        cur.execute(query, (id_contrat,))
        date_fin = cur.fetchone()
        if datetime.date.today() < date_fin[0] :
            print("Impossible d'entrer un etat des lieux dans le futur")
            return

    photo = input("Entrez le nom de la photo de l'état des lieux : ")

    kilometrage = int(input("Entrez le kilométrage du véhicule : "))
    while kilometrage <= 0:
        print("Le kilométrage doit être supérieur à zéro.")
        kilometrage = int(input("Entrez le kilométrage du véhicule : "))

    carburant = float(input("Entrez le niveau de carburant du véhicule (entre 0 et 1) : "))
    while not 0 <= carburant <= 1:
        print("Le niveau de carburant doit être compris entre 0 et 1.")
        carburant = float(input("Entrez le niveau de carburant du véhicule (entre 0 et 1) : "))

    checklist = input("Entrez la checklist de l'état des lieux : ")

    try:
        query = "INSERT INTO Etat_des_lieux (contrat, type, photo, kilometrage, carburant, checklist) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (id_contrat, type_edl, photo, kilometrage, carburant, checklist))
        connection.commit()
        print("État des lieux créé avec succès !")
    except psycopg2.Error as err:
        print(f"Erreur lors de la création de l'état des lieux : {err}")
        connection.rollback()

def menu(connection):
    logged_in = False
    user_type = None
    choice = -1
    username = ''
    while True:
        if not logged_in:
            print("\nMenu principal :")
            print("0. Se connecter")
            print("1. S’inscrire")
            print("2. Partir")
            choice = input("Choisissez une option : ")
            if choice == "0":
                username = input("Nom d'utilisateur : ")
                password = input("Mot de passe : ")
                print("iciiii")
                logged_in, user_type = login(connection, username, password)
                print(user_type)
                print(logged_in)
                if not logged_in:
                    print("Nom d'utilisateur ou mot de passe incorrect.")
            elif choice == "1":
                create_user(connection)
            elif choice == "2" :
                return
        else :
            print("\nMenu principal :")
            print("0. Déconnexion")
            print("1. Insérer un nouveau conducteur")
            print("2. Consulter les annonces")
            print("3. Insérer un nouveau commentaire")
            print("4. Consulter et annuler une réservation")
            print("5. Annuler une réservation")
            print("6. Ajouter une annonce")
            print("7. Supprimer une annonce")
            print("8. Réserver une annonce")
            print("9. Effectuer un état des lieux")

            choice = input("Choisissez une option : ")
            if choice == "0":
                logged_in = False
            elif choice == "1":
                if user_type != "entreprise":
                    print("Vous n'avez pas la permission d'effectuer cette action.")
                else:
                    insert_new_conducteur_with_input(connection, username)
            elif choice == "2":
                Consulter_Annonce(connection)
            elif choice == "3":
                insert_new_comment_with_input(connection, user_type, username)
            elif choice == "4":
                if user_type == "locataire":
                    pass
                    ##Consulter_reservation(username)
                elif user_type == "proprietaire":
                    pass
                    ##Consulter_reservation(username)
                elif user_type == "entreprise":
                    pass
                    ##Consulter_reservation(username)
                else:
                    print("Type d'utilisateur non reconnu.")
            elif choice == "5" :
                pass
            elif choice == "6" :
                pass
            elif choice == "7":
                if user_type != "proprietaire":
                    print("Vous n'avez pas la permission d'effectuer cette action.")
                else:
                    pass
                    ##supprimer_annonce(connection)
            elif choice == "8":
                if user_type == "proprietaire":
                    print("Vous n'avez pas la permission d'effectuer cette action.")
                elif user_type == "entreprise":
                    Rerserver_Voiture(connection, None, username)
                else :
                    Rerserver_Voiture(connection, username, None)
            elif choice == "9":
                Etat_des_lieux()
            else:
                print("Choix invalide. Veuillez choisir une option valide.")

def main() :
    try:
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        print("Connexion à la BDD réussie")

        menu(conn)

        conn.close()
        print("Déconnexion de la BDD réussie")

    except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type D'Exception' : ", type(error))

if __name__ == "__main__":
    main()


