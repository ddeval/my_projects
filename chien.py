class Chien():
    def __init__(self, nom, age, race):
        self.nom = nom 
        self.age = age 
        self.race = race 



def input_dog():
    nom=input("Entrez le nom du chien ")
    age=int(input("Entrez l'age du chien "))
    race=input("Entrez la race du chien ")
    chien=Chien(nom,age,race)

    return chien
    
def voir_chien(chien: Chien):
    print(f"Le chien {chien.nom} d'age: {chien.age} de race {chien.race}")

def show_menu():
    while True : 
        print("""Faites votre choix :
        1 - Ajouter le chien 
        2 - Voir les chiens
        3 - Quitter le programme""")
        choix = input("Votre choix (1|2|3) : ")

        if choix in "123" and len(choix) == 1:
            return choix
        else:
            print("Erreur, réessayez !\n\n")

if __name__ == '__main__':
    liste_chien=[]
    mon_chien=liste_chien.append(input_dog())
    voir_chien(mon_chien)
    

    while True :
        
        choix = show_menu
        

        match choix:
            case "1":
                liste_chien.append(input_dog())
            case "2":

                voir_chien(mon_chien)
                
            case "3": 
                break #ou exit() ou return



    
