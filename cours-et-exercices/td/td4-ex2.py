import psycopg2

HOST = 'localhost'
USER = 'your_user'
PASSWORD = 'your_password'
DATABASE = 'your_database'

try:
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST,DATABASE,USER,PASSWORD))
    print("Connexion ressite")
    cur = conn.cursor()

    # Fetch data line by line

    login=str(input("Entrez le nom du etudient"))
    req_add="SELECT devoir,valeur FROM etudiant e JOIN note n ON e.login=n.etudiant WHERE e.nom='%s';"%(input_nom) 
    cur.execute(req_add)
    conn.commit()

    raw = cur.fetchone()
    while raw:
        print ("[%s]|%d" % (raw[0],raw[1]))
        raw = cur.fetchone()
    conn.close()

except Exception as error:
    print("Une exception s'est produite",error)
    print("Type d'exception",type(error))

