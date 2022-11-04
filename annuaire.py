from datetime import date
from pickle import GLOBAL
import mysql.connector
my_db = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password ='',
    database='annuaire_sql')
cursor = my_db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS annuaire_sql")

query = '''
CREATE TABLE IF NOT EXISTS PERSONNE (
personne_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR (150) NOT NULL,
prenom VARCHAR (150) NOT NULL,
date_naissance DATE NOT NULL,
telephone VARCHAR (150) NOT NULL,
email VARCHAR (150) NOT NULL);'''
cursor.execute(query)
my_db.commit()

def view_all_contacts():
    query = "SELECT personne_id,nom, prenom, date_naissance,telephone,email FROM personne;"
    cursor.execute(query)
    utilisateur = cursor.fetchall()
    print(utilisateur)
    for personne_id,nom, prenom, date_naissance,telephone,email  in utilisateur:
        print(f"id:{personne_id}\n bonjour {nom} {prenom} vous êtes né le {date_naissance},votre téléphone est le {telephone} et votre email est : {email} ")

def add_contacts():
    nom=input("Rentrer le nom: ")
    prenom=input("Rentrer le prénom: ")
    date_naissance=input("Rentrer la date_naissance: ")
    telephone=input("Rentrer le telephone: ")
    email=input("Rentrer l'email: ")
    query=("""INSERT INTO personne (nom, prenom, date_naissance,telephone,email)
    VALUES (%s, %s, %s,%s,%s);""")
    values=(nom,prenom,date_naissance,telephone,email)
    cursor.execute(query, values)
    my_db.commit()

def delete_contact():
    query = "SELECT personne_id,nom FROM personne;"
    cursor.execute(query)
    utilisateur = cursor.fetchall()
    for personne_id,nom in utilisateur:
        print(f"id:{personne_id}: {nom}")
    supp=int(input("Entrer le numéro à supprimer "))
    supp = tuple(supp)
    print(type(supp))
    query ="""
    DELETE FROM PERSONNE
    WHERE personne_id = %s;"""
    cursor.execute(query, supp)
    my_db.commit()



    
# add_contacts()
# view_all_contacts()
delete_contact()

