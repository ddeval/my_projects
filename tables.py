# f-strings formatés
for i in range(0,101):
    print(f"Mon nombre bien alligné : {i:<3} (il est bien alligné)")
    print(f"Mon nombre bien alligné : {i:^3} (il est bien alligné)")
    print(f"Mon nombre bien alligné : {i:>3} (il est bien alligné)")
for i in range(0,101):
    print(f"Mon nombre bien alligné : {i:6.2f} (il est bien alligné)")

entier = 1000
taille_entier_affichage = 6
print(f"{entier:{taille_entier_affichage}}")
print(f"{entier:6}")

print("-"*80)

# print modifié
for i in range(10):
    print(i, i, sep=" ", end="abcdefg")

print("-"*80)

# Exercice tables de multiplications :

nb_table = int(input("Saisir le nombre de tables (>0) : "))

while nb_table <= 0:
    nb_table = int(input("Saisie incorrecte !!!!\nSaisir le nombre de tables (>0) : "))

print("Tables de multiplications:".center(30))
print('=' * 41)
for chiffre in range(1, 11):
    if chiffre == 1 :
        print("|", end='')
    print(f"{chiffre:3}", end="|")
print('\n=' + '=' * 40)

for table in range(1, nb_table+1):
    for chiffre in range(1, 11):
        if chiffre == 1 :
            print("|", end='')
        print(f"{table*chiffre:3}", end="|")
    print('\n+' + "---+" * 10)


# Avec un seul print et de la concatenation :

chaine = "Tables de multiplications:".center(30) + "\n"
chaine += '=' * 41  + "\n"
for chiffre in range(1, 11):
    if chiffre == 1 :
        ligne = "|"
    ligne += f"{chiffre:3}|"
chaine+= ligne + '\n=' + '=' * 40 + "\n"

for table in range(1, nb_table+1):
    for chiffre in range(1, 11):
        if chiffre == 1 :
            ligne = "|"
        ligne += f"{table*chiffre:3}|"
    chaine += ligne + '\n+' + "---+" * 10 + "\n"
print(chaine)