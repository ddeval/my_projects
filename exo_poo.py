# class Chien():
#         def __init__(self, nom, age, race):
#             self.attribut_nom = nom
#             self.attribut_age = age
#             self.attribut_race = race

# def input_chien():
#     nom = input("nom ? ")
#     age = int(input("age ? "))
#     race = input("race ? ")
#     chien = Chien(nom, age, race)
#     return chien

# def main_menu():
#     while True:
#         print("=== MENU PRINCIPAL ===")
#         print("1. Voir les chiens")
#         print("2. Ajouter les chiens")
#         print("3. Supprimer les chiens")
#         print("0. Quitter le programme")
#         choice = input("Votre choix : ")
#         if choice in "1230" and len(choice) == 1:
#             return choice
#         else:
#             print("Erreur, réessayez !\n")

# def handle_choice(choice:str, liste_chiens : list):
#     match choice :
#         case "1":
#             print("---Liste des chiens---")
#             for chien in liste_chiens:
#                 print(chien.attribut_nom, chien.attribut_age, chien.attribut_race)
#         case "2":
#             liste_chiens.append(input_chien())
#         case "3":
#             liste_chiens.pop(int(input("Veuillez saisir le numéro du chien que vous voulez supprimer : "))-1)
#         case "4" :
#             pass
#         case "0"  :
#             print("Quitter le programme")
#             return False, None
#     return True, liste_chiens
# # def afficher_chien(chien):
# #     print (f"Le chien{chien.nom} a {chien.age} ans, et est de race {chien.race}" )

# def main():

#     liste_chiens = [
#     Chien ("Rex", 5, "berger allemand"),
#     Chien("princesse", 2, "caniche"),
#     Chien ("Michel", 4, "Teckel")
#     ]
#     suivant = True
#     while suivant:
#         choice = main_menu()
#         suivant, liste_chiens = handle_choice(choice,liste_chiens)


# if __name__=="__main__":
#     main()

# mon_chien = Chien("Rex", 5, "berger allemand")
# nom_du_chien = mon_chien.attribut_nom
# print(nom_du_chien)
# print(mon_chien)
# print(mon_chien.attribut_age)


# mon_2e_chien  = Chien ("princesse", 2, "caniche")
# print(mon_2e_chien.attribut_nom, mon_2e_chien.attribut_age)

# mon_3e_chien = Chien ("Michel", 4, "Teckel")

class Compte_bancaire():
    def __init__(self, numero_compte, nom, solde):
        self.attribut_numero_compte = numero_compte
        self.attribut_nom = nom
        self.attribut_solde = solde

    def versement(self):
        versement = int(input("Veuillez saisir un versement à effectuer"))
        self.attribut_solde += versement
        

    def retrait(self):
        retrait = int(input("Veuillez saisir le montant à retirer : "))
        self.attribut_solde -= retrait
        
    def agios(self):
        if self.attribut_solde <0 :
            agios = self.attribut_solde*5/100
            print("Le montant de l'agios est de :", agios)
        else : 
            print("Il n'y a pas d'agios")

    def afficher(self):
        print(self.attribut_numero_compte, self.attribut_nom, self.attribut_solde)




def main_menu():
     while True:
         print("=== MENU PRINCIPAL ===")
         print("1. Afficher tous les mouvements")
         print("2. Afficher vos débits")
         print("3. Afficher vos retraits")
         print("4. Afficher vos agios")
         print("0. Quitter le programme")
         choice = input("Votre choix : ")
         if choice in "12340" and len(choice) == 1:
             return choice
         else:
             print("Erreur, réessayez !\n")


def handle_choice(choice: str, compte):
     match choice:
        case "1":
             print('=== Votre compte ===')
             compte.afficher()
        case "2":
             compte.versement()
             compte.afficher()
        case "3":
             compte.retrait()
             compte.afficher()
        case "4":
             compte.agios()
     return compte


def main():
    compte = Compte_bancaire("FR76....", "Olivia", 5000000)
    while True:
         choice = main_menu()
         if choice == "0":
             break
         compte = handle_choice(choice, compte)


if __name__ == "__main__":
    main()
    
