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