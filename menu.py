def show_menu():
    while True : 
        print("""Faites votre choix :
        1 - Voir le secret, 
        2 - Modifier le secret,
        3 - Quitter le programme""")
        choix = input("Votre choix (1|2|3) : ")

        if choix in "123" and len(choix) == 1:
            return choix
        else:
            print("Erreur, réessayez !\n\n")


def main():

if __name__ == "__main__":
    main()