def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Editer une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in "12340" and len(choice) == 1:
            return choice
        else:
            print("Erreur, réessayez !\n")

def handle_choice(choice, adresses):
    match choice:
        case "1":
            display_adresse(adresses)
        case "2":
            adresses[(input_adresse())]
        case "3":
             adresses.discard(input_adresse())
             adresses.add(input_adresse())
    return True, adresses

def display_adresse(adresses):
    print("=== LISTE NOMS DE FAMILLE ===")
    for adresse in adresses:
        print(adresse)

def input_adresse(adresses):
    numero_adresse=input("Saisir un numero d'adresse : ")
    compl_adresse=input("Saisir une adresse : ")
    adresses = {numero_adresse: compl_adresse, }



def main():
    adresses={}
    suivant = True
    while suivant:
        choice = main_menu()
        suivant, adresses = handle_choice(choice, adresses)


if __name__ == "__main__":
    main()
