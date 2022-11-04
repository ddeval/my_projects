age=int(input("Âge? "))
salaire=int(input("Salaire? "))
exp=int(input("Nombre d'année d'expérience? "))
if age<30 :
    print("Vous êtes trop jeune")
if salaire >4000:
    print("Salaire trop élevé")
if exp <5:
    print("Pas assez d'expérience")
if age>30 and salaire<4000 and exp>5:
    print("Bon profil")
