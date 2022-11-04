from datetime import date
import mysql.connector

my_db = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='',
    database='python_sql'
)
## 1) afficher les info de connexion
# print(my_db.get_server_info())

## 2) Récup le cursueur
cursor = my_db.cursor()

## 3) Créer une db : cursor.execute("CREATE DATABASE python_sql")

## 4) Créer une requete création de table:
# query = '''
# CREATE TABLE PERSONNE (personne_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# nom VARCHAR (150) NOT NULL,
# prenom VARCHAR (150) NOT NULL,
# date_naissance DATE NOT NULL);
# '''

## 5) Executer la requete : cursor.execute(query)

## 6) Afficher les base de données :
# cursor.execute('SHOW DATABASES;')
# for database in cursor :
#     print(f"nom bdd : {database}")

## 7) Insérer un enregistrement
# cursor.execute("""INSERT INTO personne (nom, prenom, date_naissance)
# VALUES ('bas', 'a', '2010-01-01');""")

## 8) Insérer avec des valeurs dynamiques (tuples)
# query = ''' INSERT INTO personne (nom, prenom, date_naissance)
# VALUES (%s, %s, %s);'''
# nom = 'Robert'
# prenom = 'Deniro'
# date_naissance = date(2022, 1, 1)

# values = (nom, prenom, date_naissance)
# cursor.execute(query, values)

## 9) Insérer avec des valeurs dynamiques (dico)
# query = ''' INSERT INTO personne (nom, prenom, date_naissance)
# VALUES (%(nom)s, %(prenom)s, %(date_naissance)s);'''
# ma_personne = {
#     'nom' : 'Obama',
#     'prenom' : 'Michelle',
#     'date_naissance' : date(1900, 1, 1)
# }
# cursor.execute(query, ma_personne)

## 10) Mettre à jour
# query = "UPDATE personne SET date_naissance = %s WHERE personne_id = %s;"
# cursor.execute(query, (date(1980, 1, 1), 6))

## 11) Insérer plusieurs à la fois
# query = ''' INSERT INTO personne (nom, prenom, date_naissance)
# VALUES (%s, %s, %s);'''

# values = [
#     ('Bernard', 'Arnault', date(1950, 1, 1)),
#     ('Ana', 'lisa', date(1970, 1 ,1)),
#     ('jb', 'ZHUVZUEFHZE', date(1963, 1, 2))
# ]
# cursor.executemany(query, values)

## 12)Lire les enregistrement un à un
# query = "SELECT nom, prenom FROM personne;"
# cursor.execute(query)

# while True :
#     utilisateur = cursor.fetchone()
#     if utilisateur is None :
#         break
#     print(utilisateur)

## 13) Lire tous les enregistrement d'un coup
# query = "SELECT nom, prenom, date_naissance FROM personne;"
# cursor.execute(query)
# utilisateur = cursor.fetchall()
# print(utilisateur)
# # pour imprimer proprement
# for nom, prenom, date_naissance in utilisateur:
#     print(f"bonjour {nom} {prenom} vous êtes né le {date_naissance}")

## 14) Lire certains enregistrements, et affiher le reste
# query = "SELECT nom, prenom FROM personne;"
# cursor.execute(query)
# two_first_people = cursor.fetchmany (size = 2)
# last_people = cursor.fetchall() # pour recup le reste
# print(two_first_people)
# print(last_people)

## 15) Annuler la transaction
# my_db.rollback()

## 16) Valider la transaction
# my_db.commit()

## 17) Afficher le nb de lignes affectées par la dernière requete executée
# print (cursor.rowcount)

## 18) fermer  le curseur et la db, sinon utiliser "with" tout en haut
# cursor.close()
# my_db.close()

