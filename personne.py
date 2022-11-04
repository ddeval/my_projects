class Personne:
    def __init__(self, nom, prenom, tel, email):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email

    def __str__(self):
        return f" nom : {self.nom}\n prénom : {self.prenom}\n téléphone : {self.tel}\n mail : {self.email}"


class Travailleur(Personne):
    def __init__(self, nom, prenom, tel, email, nom_entreprise, adresse_entreprise, tel_pro):
        super().__init__(nom, prenom, tel, email)
        self.nom_entreprise = nom_entreprise
        self.adresse_entreprise = adresse_entreprise
        self.tel_pro = tel_pro

    def __str__(self):
        return super().__str__()+f" nom_entreprise: {self.nom_entreprise}\n adresse_entreprise: {self.nom_entreprise}\n tel_pro: {self.tel_pro}"

class Scientifique(Travailleur):
    def __init__(self, nom, prenom, tel, email, nom_entreprise, adresse_entreprise, tel_pro,disciplines:list,type_de_scientifique:list):
        super().__init__(nom, prenom, tel, email, nom_entreprise, adresse_entreprise, tel_pro)
        self.disciplines = disciplines
        self.type_de_scientifique= type_de_scientifique
        

    def __str__(self):
        return super().__str__()+f"\n disciplines: {', '.join(self.disciplines)}\n type_de_scientifique: {', '.join(self.type_de_scientifique)}"

if __name__ == "__main__":
    Dupont = Personne("Dupont", "Pierre", "04 73 30 96 40",
                      "pepette@princess.com")
    Dupont2 = Travailleur("Dupont", "Pierre", "04 73 30 96 40",
                          "pepette@princess.com", "Axa", "Rue du chien", "04-73-30-32-33")
    Dupont3= Scientifique("Dupont", "Pierre", "04 73 30 96 40",
                          "pepette@princess.com", "Axa", "Rue du chien", "04-73-30-32-33",["Physique","Chimie"],["Theorique"])

    print(Dupont)
    print(Dupont2)
    print(Dupont3)

