




# def show_menu():
#     while True : 
#         print("""Faites votre choix :
#         1 - Voir les noms de famille, 
#         2 - Ajouter un nom de famille,
#         3 - Editer le nom de famille,
#         4 - Supprimer un nom de famille.                          """)
#         choix = input("Votre choix (1|2|3|4) : ")

#         if choix in "1234" and len(choix) == 1:
#             return choix
#         else:
#             print("Erreur, réessayez !\n\n")

nom_de_famille=set()

def voir_nom_famille():
    print(nom_de_famille)
    


def ajouer_nom_de_famille():
    nom_de_famille=set()
    nom=input("Veuillez entrer un nom de famille\n")
    nom_de_famille.add(nom)
    return nom_de_famille
                    

def modifier_nom_de_famille(data):
    print(nom_de_famille)
    data=input("Ecrivez le nom à modifier")
    nom_de_famille.remove(data)
    nw_nom_de_famille=input("Ecrivez le nom à modifier")
    nom_de_famille.add(nw_nom_de_famille)


def saisie_menu():
    while True:
        print("[1] Voir les noms de famille\n[2] Ajouter un nom de famille\n[3] Editer le nom de famille\n")
        choix = input("Votre choix : ")
        
        
        match choix:
            case "1":
                return voir_nom_famille()
            case "2":
                return ajouer_nom_de_famille()
            case "3":
                return modifier_nom_de_famille()
            case _:
                print("Votre choix ne correspond pas")
    

def main():
    saisie_menu()
if __name__ == "__main__":
    main()