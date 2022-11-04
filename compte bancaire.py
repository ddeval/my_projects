class CompteBancaire():
    def __init__(self, numero_compte, nom, solde):
        self.numero_compte = numero_compte
        self.nom = nom 
        self.solde = solde 

    def versement(self,versement):
        versement = int(input("Veuillez saisir un versement à effectuer"))
        self.solde = self.solde+versement
        return self.solde

    def retrait(self,retrait):
        retrait=int(input("Veuillez saisir un versement à effectuer"))
        self.solde = self.solde-retrait
        return self.solde

    def agios(self):
        if self.solde<0:
            self.solde=self.solde-self.solde*0.05
        return self.solde
    
    def afficher_compte(self):
        print(f"le numéro de compte est: {self.numero_compte}, le nom du client est {self.nom}, le solde est {self.solde}")

def input_compte():
        numero_compte = int(input("Numéro de compte : "))
        nom = input("Nom : ")
        solde = int(input("Solde: "))
        cb = CompteBancaire(numero_compte, nom, solde)
        return cb  

def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les comptes")
        print("2. Ajouter un versement")
        print("3. comptabiliser un retrait")
        print("4. Gérer des agios")
        print("0. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in "12340" and len(choice) == 1:
            return choice
        else:
            print("Erreur, réessayez !\n")

def handle_choice(choice: str, list_comptes: list):
    match choice:
        case "1":   
            CompteBancaire.afficher_compte()
        case "2":
            CompteBancaire.versement()
        case "3":
            CompteBancaire.retrait()
        case "4":
            CompteBancaire.agios()
    return list_comptes

    
def main():
    comptes = CompteBancaire(5632,"Dupont",450)
    
    while True:
        choice = main_menu()
        if choice == "0":
            break
    comptes = handle_choice(choice, comptes)

if __name__ == "__main__":
    main()

# dupont=CompteBancaire(5623,"Dupont",450)
# dupont.versement(50)
# print(dupont.solde)
# dupont.retrait(100)
# print(dupont.solde)
# dupont.agios()
# print(dupont.solde)
# dupont.afficher()

    
    


